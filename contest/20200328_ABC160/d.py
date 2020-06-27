# -*- coding: utf-8 -*-
N, X, Y = map(int, input().split())

distances = [0 for i in range(1, N)]

middle_point = X+Y-1

if middle_point % 2 == 0:
    for i in range(1, X):
        for j in range(i+1, middle_point+1):
            distance = j-1
            distaces[distance] += 1
        for j in range(middle_point+1, N+1):
            distance = (X-i+1) + abs(Y-j)
            distaces[distance] += 1
    for i in range(X+1, )
else:


