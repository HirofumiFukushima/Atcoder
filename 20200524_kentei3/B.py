# -*- coding: utf-8 -*-

N, M, Q = map(int, input().split())

# 各人の解けた問題
person_scores = [[] for n in range(N)] 
# 核問題のスコア
problem_scores = [N for m in range(M)]
# query
query_list = []
for q in range(Q):
    query_list.append(list(map(int, input().split())))

for query in query_list:
    if query[0] == 1:
        score = sum(problem_scores[m-1] for m in person_scores[query[1]-1])
        print(score)
    else:
        problem_scores[query[2]-1] -= 1
        person_scores[query[1]-1].append(query[2])