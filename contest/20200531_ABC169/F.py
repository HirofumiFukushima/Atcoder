# -*- coding: utf-8 -*-
N, S = map(int, input().split())
A = list(map(int, input().split()))
A = list(sorted(A))

mod = 998244353

# find subset =S
def sum_subset(S):
    subsets = [set() for i in range(0, S+1)]
    j = 0
    for i in range(1, S+1):
        # 同じ数字を探す
        if j < N and A[j] == i:
            start = j
            while j < N and A[j] == i:
                j += 1
            end = j-1
            subsets[i] = subsets[i] | set(tuple([j]) for j in range(start, end+1]])

        # i = a + b となる組み合わせ
        for a in range(1,i):
            b = i-a
            subsets_a_b = []
            for s_a in subsets[a]:
                for s_b in subsets[i-a]:
                    if len(set(s_a) & set(s_b)) == 0:
                        subsets_a_b.append(tuple(list(s_a)+list(s_b)))
            subsets_a_b = list(set(tuple(sorted(s)) for s in subsets_a_b))
            subsets_a_b = 
    return subsets[S]

subsets = sum_subset(S)
# 重複を除く
subsets_sets = [tuple(sorted(s)) for s in subsets]
subsets_sets = set(subsets_sets)


score_mod = 0
for subset in subsets_sets:
    score_mod = (score_mod+pow(2,N-len(subset)))%mod

print(score_mod)