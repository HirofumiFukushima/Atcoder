# -*- coding: utf-8 -*-

T = list(input())

T = [t if t != '?' else 'D' for t in T ]

print(''.join(T))