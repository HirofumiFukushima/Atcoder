# -*- coding: utf-8 -*-

N = int(input())

kaibun_candidates = []
for n in range(N):
    kaibun_candidates.append(list(input()))

# S_iとS_{N-i}を構築していく形.
# i行目とN-1行目に同じ文字があればok.

kaibun = ['*' for n in range(N)]

for i in range(int(N/2)):
    S_i = kaibun_candidates[i]
    S_N_i = kaibun_candidates[N-i-1]

    kyoutsu_moji = list(set(S_i) & set(S_N_i))
    if list(kyoutsu_moji) != []:
        kaibun[i] = kyoutsu_moji[0]
        kaibun[N-1-i] = kyoutsu_moji[0]
    else:
        print(-1)
        exit(0)

if N == 1:
    kaibun[0] = kaibun_candidates[0][0]
if N != 1 and N%2 == 1:
    kaibun[int(N/2)] = kaibun_candidates[int(N/2)][0]

print(''.join(kaibun))