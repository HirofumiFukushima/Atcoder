# -*- coding: utf-8 -*-
import collections
def find(tuple_list, num, top_idx):
    length = len(tuple_list)

    if length == 0:
        return top_idx, False

    if length == 1:
        hikaku = tuple_list[0][0]
        if num == hikaku:
            return top_idx, True
        elif num < hikaku:
            return top_idx-1, False
        elif num > hikaku:
            return top_idx, False
    
    if length == 2:
        hikaku1 = tuple_list[0][0]
        hikaku2 = tuple_list[1][0]
        if num == hikaku1:
            return top_idx, True
        elif num == hikaku2:
            return top_idx+1, True
        elif num < hikaku1:
            return top_idx-1, False
        elif hikaku1 < num < hikaku2:
            return top_idx, False
        elif hikaku2 < num:
            return top_idx+1, False

    place = int(length/2)
    hikaku = tuple_list[place][0]
    if num == hikaku:
        return top_idx+place, True
    elif num < hikaku:
        return find(tuple_list[:place], num, top_idx)
    elif num > hikaku:
        return find(tuple_list[place+1:], num, top_idx+place+1)


N = int(input())
A = list(map(int, input().split()))
A_amount = list(collections.Counter(A).items())
A_amount = list(sorted(A_amount, key=lambda x:x[0]))

result = sum(A)

Q = int(input())
for q in range(Q):
    B, C = map(int, input().split())
    B_idx, is_B_exist = find(A_amount, B, 0)
    if is_B_exist:
        old_tuple = A_amount[B_idx]
        C_idx, is_C_exist = find(A_amount, C, 0)
        if is_C_exist:
            new_tuple = (C, A_amount[B_idx][1]+A_amount[C_idx][1])
            A_amount[C_idx] = new_tuple
            A_amount_before = A_amount[:B_idx]
            A_amount_after = A_amount[B_idx+1:]
            A_amount_before.extend(A_amount_after)
            A_amount = A_amount_before
        else:
            new_tuple = (C, A_amount[B_idx][1])
            if B_idx < C_idx:
                A_amount_1 = A_amount[:B_idx]
                A_amount_2 = A_amount[B_idx+1:C_idx+1]
                A_amount_3 = A_amount[C_idx+1:]
                A_amount_1.extend(A_amount_2)
                A_amount_1.append(new_tuple)
                A_amount_1.extend(A_amount_3)
            else:
                A_amount_1 = A_amount[:C_idx+1]
                A_amount_2 = A_amount[C_idx+1:B_idx]
                A_amount_3 = A_amount[B_idx+1:]
                A_amount_1.append(new_tuple)
                A_amount_1.extend(A_amount_2)
                A_amount_1.extend(A_amount_3)
            A_amount = A_amount_1
    
        result += (C-B)*old_tuple[1]
    
    print(result)