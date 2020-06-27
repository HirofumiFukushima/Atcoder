# -*- coding: utf-8 -*-
N = int(input())
t = []
for i in range(N):
    t.append(int(input()))

min_meat_time = sum(t)+1
for bit in range(2**N):
    meat1 = []
    meat2 = []
    for shift in range(N):
        if (bit>>shift)&1:
            meat1.append(t[shift])
        else:
            meat2.append(t[shift])
        
    min_meat_time = min(min_meat_time, max(sum(meat1), sum(meat2)))

print(min_meat_time)