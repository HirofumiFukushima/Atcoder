# -*- coding: utf-8 -*-

max_value = pow(10, 100)

N, L = map(int, input().split())
x_list = list(map(int, input().split()))
is_x_exist = [False for _ in range(L+4)]
for x in x_list:
    is_x_exist[x] = True
T1,T2,T3 = list(map(int, input().split()))

# 余分にとる
min_time = [max_value for l in range(L+4)]

# 距離lにいるときのl+1~l+4までの最小時間を求める

for l in range(L):
    if l == 0:
        min_time[0] = 0
    # 行動1について考える
    if not is_x_exist[l+1]:  # l+1にハードルがない場合
        min_time[l+1] = min(min_time[l+1], min_time[l]+T1)
    else:                  # l+1にハードルがある場合
        min_time[l+1] = min(min_time[l+1], min_time[l]+T1+T3)
    # 行動2について考える
    if not is_x_exist[l+2]:
        min_time[l+2] = min(min_time[l+2], min_time[l]+T1+T2)
    else:
        min_time[l+2] = min(min_time[l+2], min_time[l]+T1+T2+T3)
    # 行動3について考える
    if not is_x_exist[l+4]:
        min_time[l+4] = min(min_time[l+4], min_time[l]+T1+(3*T2))
    else:
        min_time[l+4] = min(min_time[l+4], min_time[l]+T1+(3*T2)+T3)

# 飛び越えた場合を考える
min_time[L] = min(min_time[L], 
                  min_time[L-3]+int(T1/2)+int(5*T2/2),
                  min_time[L-2]+int(T1/2)+int(3*T2/2),
                  min_time[L-1]+int(T1/2)+int(  T2/2))

print(min_time[L])