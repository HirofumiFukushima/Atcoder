# -*- coding: utf-8 -*-
import math

A,B,H,M = map(int, input().split())

A_ratio = (60*H+M)/720
B_ratio = M/60

sa = abs(A_ratio - B_ratio)

theta = min(2*math.pi*sa, 2*math.pi*(1-sa))

C = math.sqrt(pow(A,2)+pow(B,2) - (2*A*B*math.cos(theta)))

print(C)