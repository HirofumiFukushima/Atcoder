# -*- coding: utf-8 -*-
A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V < W or abs(A-B) > (V-W)*T:
    print('NO')
else:
    print('YES')