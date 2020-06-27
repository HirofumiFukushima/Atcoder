# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split()))

all_xor = 0
for i in range(N):
    all_xor = all_xor^a[i]

answer = [a[i]^all_xor for i in range(N)]

print(' '.join(map(str, answer)))