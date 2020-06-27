# -*- coding: utf-8 -*-
A,B = input().split()
A = int(A)
B_i, B_d = B.split('.')
B_i = int(B_i)
# calc b_d
B_d = list(B_d)
B_100 = 100*B_i + int(B_d[0])*10 + int(B_d[1])

result_100 = A * B_100

if result_100 >= 100:
    print(str(result_100)[:-2])
else:
    print(0)