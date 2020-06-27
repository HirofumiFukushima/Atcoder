# -*- coding: utf-8 -*-
X, Y, A, B, C = map(int, input().split())
red_oishisa = list(map(int, input().split()))
green_oishisa = list(map(int, input().split()))
no_oishisa = list(map(int, input().split()))

red_oishisa = list(sorted(red_oishisa))[::-1]
green_oishisa = list(sorted(green_oishisa))[::-1]
no_oishisa = list(sorted(no_oishisa))[::-1]

oishisa_s = []

i=1
j=1
k=1
while(True):
    if len(oishisa_s) == X+Y:
        break
    
    hikaku_dict = dict()
    if i <= X:
        hikaku_dict['red'] = red_oishisa[i-1]
    if j <= Y:
        hikaku_dict['green'] = green_oishisa[j-1]
    if k <= C:
        hikaku_dict['no'] = no_oishisa[k-1]
    
    max_key, max_value = max(hikaku_dict.values(), key=lambda x:x[1])
    oishisa_s.append(max_value)
    if max_key == 'red':
        i += 1
    elif max_key == 'green':
        j += 1
    elif max_key == 'no':
        k += 1

print(sum(oishisa_s))

# eat_oishisas_red = red_oishisa[:X]
# eat_oishisas_green = green_oishisa[:Y]

# i=1
# j=1
# k=1
# while(True):
#     if i > A:
#         break
#     elif j > B:
#         break
#     elif k > C:
#         break
#     elif min([eat_oishisas_red[-i], eat_oishisas_green[-j]]) >= no_oishisa[k-1]:
#         break

#     if eat_oishisas_red[-i] <= eat_oishisas_green[-j]:
#         eat_oishisas_red[-i] = no_oishisa[k-1]
#         i += 1
#     else:
#         eat_oishisas_green[-j] = no_oishisa[k-1]
#         j += 1
#     k += 1

# rint(sum(eat_oishisas_green) + sum(eat_oishisas_red))
