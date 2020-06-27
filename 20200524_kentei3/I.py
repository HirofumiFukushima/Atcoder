# -*- coding: utf-8 -*-

import copy
# 置換を覚えておけばよい。
# 元のindexをkey, 置換後のindexをvalueとする辞書

def element_matrix(i,j):
    return N*(i-1)+(j-1)

N = int(input())
row_replace_dict = {i:i for i in range(1,N+1)}
col_replace_dict = {i:i for i in range(1,N+1)}
Q = int(input())
query_list = []
for q in range(Q):
    query_list.append(list(map(int, input().split())))

is_reversed = False

for query in query_list:
    if (not is_reversed and query[0] == 1) or \
       (    is_reversed and query[0] == 2):
        A = query[1]
        B = query[2]
        (row_replace_dict[A], row_replace_dict[B]) = \
        (row_replace_dict[B], row_replace_dict[A])
    elif (not is_reversed and query[0] == 2) or \
         (    is_reversed and query[0] == 1):
        A = query[1]
        B = query[2]
        (col_replace_dict[A], col_replace_dict[B]) = \
        (col_replace_dict[B], col_replace_dict[A])
    elif query[0] == 3:
        is_reversed = not is_reversed
    elif query[0] == 4:
        A = query[1]
        B = query[2]
        if not is_reversed:
            print(element_matrix(row_replace_dict[A], col_replace_dict[B]))
        else:
            print(element_matrix(row_replace_dict[B], col_replace_dict[A]))
