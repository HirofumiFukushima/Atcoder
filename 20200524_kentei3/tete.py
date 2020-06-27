import re
import torch
import torch.nn as nn
import torch.functional as F
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

from bpemb import BPEmb

train_df = pd.read_csv("/kaggle/input/tweet-sentiment-extraction/train.csv")
test_df = pd.read_csv("/kaggle/input/tweet-sentiment-extraction/test.csv")
sample_output_df = pd.read_csv("/kaggle/input/tweet-sentiment-extraction/sample_submission.csv")

def jaccard(str1, str2): 
    a = set(str1.lower().split()) 
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def jaccard_list(list1, list2): 
    a = set(list1) 
    b = set(list2)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def preprocess(tweet):
    tweet = tweet.split()
    # remove url, hash tag, account.
    stop_words = ['http', 'www', '#', '@', r'_.+']
    # stop_words = []
    new_tweet = [
        word for word in tweet
        if not any([re.match(stop, word) for stop in stop_words])
    ]
    return " ".join(new_tweet)

neutral_data = train_df[train_df['sentiment'] == 'neutral']

# check if preprocessing is effective
total_neutral = len(neutral_data)
diff = 0
sum_jaccard = 0
for index, row in neutral_data.iterrows():
    if type(row['text']) == str:
        ed_text = preprocess(row['text'])
        target_text = row['selected_text']
        sum_jaccard += jaccard(ed_text, target_text)
        if ed_text != target_text:
            diff += 1

# data loader
class TweetSentimentExtractionDataset(torch.utils.data.Dataset):
    def __init__(self, data_df, transform_text=None, transform_sentiment=None, extraction_mode='raw'):
        self.transform_text = transform_text
        self.transform_sentiment = transform_sentiment
        self.extraction_mode = extraction_mode
        
        # error handling
        if type(data_df) != pd.core.frame.DataFrame:
            raise ValueError('input is not Dataframe.')
        elif not any([column in data_df.columns for column in ['text', 'selected_text', 'sentiment']]):
            raise ValueError('column of Dataframe is insufficient.')
            
        self.n_data = len(data_df)
        # input
        self.text = []
        # targets
        self.sentiment = []
        self.extraction = []
        for index, row in data_df.iterrows():
            if not any([type(row['text'])==str, type(row['selected_text'])==str]):
                raise ValueError('Invalid row in input_df. index: {}'.format(index))
            self.text.append(row['text'])
            self.sentiment.append(row['sentiment'])
            self.extraction.append(row['selected_text'])
            
    def __len__(self):
        return self.n_data
    
    def __getitem__(self, idx):
        text = self.text[idx]
        extraction = self.extraction[idx]
        sentiment = self.sentiment[idx]
        
        def _extraction_start_end(text_idxs, extraction_idxs):
            for i in range(len(text_idxs)-len(extraction_idxs)+1):
                if torch.all(text_idxs[i:i+len(extraction_idxs)] == extraction_idxs):
                    new_extraction = {'start':i, 'end':i+len(extraction_idxs)-1}
                    break
            # not matched
            else: new_extraction = {'start':-1, 'end':-1}
            return new_extraction

        def _extraction_labelling(text_idxs, extraction_idxs):
            extraction_span = _extraction_start_end(text_idxs, extraction_idxs)
            new_extraction = torch.zeros(len(text_idxs), dtype=torch.long)
            if extraction_span['start'] != -1:
                new_extraction[extraction_span['start']:extraction_span['end']+1] = torch.ones(len(extraction_idxs), dtype=torch.long)
            else:
                torch.ones(len(text_idxs), dtype=torch.long)
            return new_extraction

        if self.transform_text:
            new_text = self.transform_text(text)
            new_extraction = self.transform_text(extraction)
            # in mode='label' or 'span', detect where extraction in text
            if self.extraction_mode == 'span':
                new_extraction = _extraction_start_end(new_text, new_extraction)
            elif self.extraction_mode == 'label':
                new_extraction = _extraction_labelling(new_text, new_extraction)
        else:
            new_text = text
            new_extraction = extraction
                
        if self.transform_sentiment:
            new_sentiment = self.transform_sentiment(sentiment)
            
        text_length = torch.tensor(len(new_text), dtype=torch.long)
        
        return text_length, new_text, new_sentiment, new_extraction

# transform
class SentimentBinalizer():
    def __init__(self):
        pass
    def __call__(self, sentiment):
        sentiment_idx_dict = {
            'negative': 0,
            'neutral': 1,
            'positive': 2
        }
        return torch.tensor(sentiment_idx_dict[sentiment], dtype=torch.long)
    
class TweetTokenizer():
    def __init__(self, dim=50, vocab_size=10000, mode='get_id'):
        self.dim = dim
        self.vocab_size = vocab_size
        self.bpemb_en = BPEmb(lang="en", dim=dim, vs=vocab_size)
        self.embedding_weight = self.bpemb_en.vectors
        self.mode = mode
    
    def __call__(self, tweet, mode='get_id'):
        if mode == 'get_id':
            return torch.tensor(self.bpemb_en.encode_ids(tweet), dtype=torch.long)
        elif mode == 'raw':
            return self.bpemb_en.encode(tweet)
        else:
            raise ValueError('Invalid mode')

# padding at dataloader
def padding_sentence(batch):
    '''
    input:
        batch: list of (text, sentiment, extraction) (numpy)
            text: [timestep] (idxs of subwords)
            sentiment: [dim] (0: negative, ... ,2:positive)
            extraction: [timestep] ("extracted" labelling)
            
    '''
    # unpack batch
    text_length, text, sentiment, extraction = list(zip(*batch))
    # detect max length
    max_length = max(text_length)
    # padding
    text = [tweet+1 for tweet in text]
    text = [torch.cat((tweet, torch.zeros(max_length-len(tweet), dtype=torch.long)), dim=0)
            if len(tweet) != max_length else tweet
            for tweet in text]
    extraction = [torch.cat((tweet, torch.zeros(max_length-len(tweet), dtype=torch.long)), dim=0)
                  if len(tweet) != max_length else tweet
                  for tweet in extraction]
    
    return torch.stack(text_length), torch.stack(text), torch.stack(sentiment), torch.stack(extraction)

class LSTM_Attention_WithSelectLabel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, n_sentiment_label=3, embedding_weight=None):
        super(LSTM_Attention_WithSelectLabel, self).__init__()
        self.n_sentiment_label = n_sentiment_label
        self.vocab_size = vocab_size
        # embedding layer
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        if embedding_weight is not None:
            self.embedding.weight = nn.Parameter(embedding_weight)
            self.embedding.requires_grad = False
        # LSTM layer
        self.biLSTM_1 = nn.LSTM(embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.biLSTM_2 = nn.LSTM(hidden_dim*2, hidden_dim, batch_first=True, bidirectional=True)
        # calc labelling_score
        self.fc_label_1 = nn.Linear(hidden_dim*2, hidden_dim*2)
        self.relu = nn.ReLU()
        self.fc_label_2 = nn.Linear(hidden_dim*2, n_sentiment_label)
        self.sigmoid = nn.Sigmoid()
        # calc attention
        self.softmax = nn.Softmax(dim=1)
        self.fc_sentiment_1 = nn.Linear(hidden_dim*2, hidden_dim*2)
        self.fc_sentiment_2 = nn.Linear(hidden_dim*2, 1)
        
    def forward(self,inp):
        # LSTM
        emb = self.embedding(inp)
        hidden1, _ = self.biLSTM_1(emb)
        hidden2, _ = self.biLSTM_2(hidden1)
        # labbeling score
        batch_size, timestep = hidden2.shape[0:2]
        hidden = hidden2.reshape(-1, hidden2.shape[2])
        label_score = self.fc_label_2(self.relu(self.fc_label_1(hidden))).reshape(batch_size, timestep, self.n_sentiment_label)
        label_prob = self.sigmoid(label_score)
        # attention
        attention = self.softmax(label_score)
        context_vec = torch.einsum('nth,nta->nah', hidden2, attention)
        context_vec = context_vec.reshape(-1, context_vec.shape[2])
        sentiment_score = self.fc_sentiment_2(self.relu(self.fc_sentiment_1(context_vec))).reshape(batch_size, self.n_sentiment_label)
        sentiment_prob = self.softmax(sentiment_score)
        
        return label_prob, sentiment_prob

class SentimentExtractionLoss(nn.Module):
    def __init__(self, n_semtiment_label, alpha=0.5):
        super(SentimentExtractionLoss, self).__init__()
        self.n_sentiment_label = n_semtiment_label
        self.alpha = alpha
    
    def forward(self, text_length, true_extract, pred_extract, true_sentiment, pred_sentiment):
        # label loss
        pred_extract = torch.stack([pred_extract[i,:,sent] for i, sent in enumerate(true_sentiment)])
        nll_loss_extract = - (true_extract * torch.log(pred_extract)) - ((1-true_extract) * torch.log(1-pred_extract))
        for n in range(len(text_length)):
            nll_loss_extract[n,text_length[n]:] = 0
        ave_nll_loss_extract_per_data = torch.sum(nll_loss_extract, dim=1) / text_length
        label_loss = torch.mean(ave_nll_loss_extract_per_data)
        # sentiment loss
        nll_loss_sentiment = - torch.eye(self.n_sentiment_label)[true_sentiment] * torch.log(pred_sentiment)
        sentiment_loss = torch.mean(torch.sum(nll_loss_sentiment, dim=1))
        
        return (self.alpha*label_loss) + ((1-self.alpha)*sentiment_loss)