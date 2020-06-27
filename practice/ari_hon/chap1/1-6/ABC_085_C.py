# -*- coding: utf-8 -*-
N,Y = map(int, input().split())

for n_10000 in range(int(Y/10000)+1):
    y_10000 = n_10000*10000
    for n_5000 in range(int((Y-y_10000)/5000)+1):
        y_5000 = n_5000*5000
        
        n_1000 = N-n_10000-n_5000
        if n_1000 >= 0 and Y-y_10000-y_5000 == 1000*n_1000:
            print('{} {} {}'.format(n_10000, n_5000, n_1000))
            exit(0)

print('-1 -1 -1')