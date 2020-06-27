# -*- coding: utf-8 -*-
K, S = map(int, input().split())

n_int = 0

for z in range(min(K, S)+1):
    for y in range(min(K, S-z)+1):
        if S-y-z <= K:
            n_int += 1

print(n_int)