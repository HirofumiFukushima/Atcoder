# -*- coding: utf-8 -*-
import collections
N = int(input())
A = list(map(int, input().split()))
A_amount = dict(collections.Counter(A))

result = sum(A)

Q = int(input())
for q in range(Q):
    B, C = map(int, input().split())
    B_elem = A_amount.get(B, None)
    if B_elem is not None:
        C_elem = A_amount.get(C, None)
        if C_elem is not None:
            A_amount.pop(B)
            A_amount[C] = B_elem+C_elem
        else:
            A_amount.pop(B)
            A_amount[C] = B_elem

        result += (C-B)*B_elem

    print(result)