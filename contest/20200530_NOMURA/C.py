# -*- coding: utf-8 -*-
import math

def floor_div(x,d):
    if x%d != 0:
        return int(x/d)+1
    else:
        return int(x/d)

N = int(input())

A = list(map(int, input().split()))

n_not_leaf = 0
sum_node = 0

num_node = [0 for d in range(N+1)]
max_node = [0 for d in range(N+1)]

# 各層のnodeのmax個を計算
for d in range(N+1):
    if d == 0:
        max_node[0] = 1
    else:
        max_node[d] = (max_node[d-1]-A[d-1])*2
    
    if d != N and max_node[d]-A[d] < 1:
        print(-1)
        exit()
if max_node[N]-A[N] < 0:
    print(-1)
    exit()


for d in reversed(range(N+1)):
    if d == N:
        num_node[N] = min(A[N], max_node[N])
    else:        
        if floor_div(num_node[d+1],2)+A[d] > max_node[d]:
            print(-1)
            exit()
        else:
            num_node[d] = min(num_node[d+1]+A[d], max_node[d])

print(sum(num_node))