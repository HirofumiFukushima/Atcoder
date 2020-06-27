# -*- coding: utf-8 -*-

mod = 1000000007

N = int(input())

A_list = [0 for n in range(N)]
B_list = [0 for n in range(N)]
iwashi_aishou = [[True for n in range(N)] for n in range(N)]
for n in range(N):
    A_list[n], B_list[n] = map(int, input().split())

for n in range(N):
    for i in range(n):
        if (A_list[n]*A_list[i])+(B_list[n]*B_list[i]) == 0:
            iwashi_aishou[n][i] = False

# 計算量オーバー
# def baaino_kazu(idx_list):
#     if len(idx_list) == 1:
#         return 2
#     else:
#         max_idx = idx_list[-1]
#         # max_idxを入れない場合
#         kazu_without_maxidx = baaino_kazu(idx_list[:-1])
#         # max_idxを入れる場合
#         waru_aishou = [i for i in range(max_idx) if iwashi_aishou[max_idx][i] == False]
#         waru_aishou.append(max_idx)
#         nokori = list(set(idx_list) - set(waru_aishou))
#         nokori.sort()
#         kazu_with_maxidx = baaino_kazu(nokori)

#         return (kazu_with_maxidx+kazu_without_maxidx)%mod