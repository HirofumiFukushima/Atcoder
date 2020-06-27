# -*- coding: utf-8 -*-

N = int(input())

mod = N%10
if mod in [2,4,5,7,9]:
    print('hon')
elif mod in [0,1,6,8]:
    print('pon')
else:
    print('bon')