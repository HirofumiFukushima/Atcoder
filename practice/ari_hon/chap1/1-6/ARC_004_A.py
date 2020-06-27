# -*- coding: utf-8 -*-
def distance(a, b):
  square = pow(a[0]-b[0],2)+pow(a[1]-b[1],2)
  return pow(square, 1/2)
 
N = int(input())
 
dots = []
for i in range(N):
  dots.append(list(map(int, input().split())))
  
max_length = 0
for i in range(N):
  for j in range(i):
    length = distance(dots[i], dots[j])
    if max_length < length:
      max_length = length

print('{}\n'.format(max_length))