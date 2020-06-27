# -*- coding: utf-8 -*-
# ABCD
S = list(map(int, list(input())))

for bit in range(2**3):
    formula_sum = S[0]
    formula = str(S[0])
    for shift in range(3):
        # 1だったら+
        if (bit >> shift)&1:
            formula_sum += S[shift+1]
            formula += '+{}'.format(S[shift+1])
        else:
            formula_sum -= S[shift+1]
            formula += '-{}'.format(S[shift+1])
    
    if formula_sum == 7:
        print(formula+'=7')
        exit(0)