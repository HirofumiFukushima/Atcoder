# -*- coding: utf-8 -*-

K = int(input())
S = input()

if len(S) > K:
    print('{}...'.format(S[:K]))
else:
    print(S)
