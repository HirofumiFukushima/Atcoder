# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

if 0 in set(A):
    print(0)
    exit()

result = 1
for i in range(N):
    result *= A[i]
    if result > pow(10,18):
        print(-1)
        exit()

print(result)