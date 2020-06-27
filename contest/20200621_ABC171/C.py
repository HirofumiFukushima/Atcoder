# -*- coding: utf-8 -*-
alphabet = 'abcdefghijklmnopqrstuvwxyz'
N = int(input())

n = N
name = []
while n != 0:
    name.append(alphabet[(n%26)-1])
    if n%26==0:
        n = int(n/26)-1
    else:
        n = int(n/26)


print(''.join(name[::-1]))