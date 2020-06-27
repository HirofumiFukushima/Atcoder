# -*- coding: utf-8 -*-

A,R,N = map(int, input().split())

max_value = pow(10,9)

if R == 1:
    print(A)

# R>=2のときは、順番に足して行った方がoverflowを起こしにくい
else:
    now_value = A
    for n in range(N):
        if now_value > max_value:
            print('large')
            exit(0)
        elif n != N-1:
            now_value *= R
    
    print(now_value)