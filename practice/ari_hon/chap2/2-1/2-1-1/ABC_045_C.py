# -*- coding: utf-8 -*-
import time
S = input()

n = len(S)

start = time.time()
sum_formula = 0
# bit全探索
for bit in range(2 ** (n-1)):
    nums = []
    # 何ビットシフトさせるか
    num = S[0]
    for shift in range(n-1):
        if not ((bit >> shift)&1):
            num = num + S[shift+1]
        else:
            nums.append(int(num))
            num = S[shift+1]
    nums.append(int(num))
    sum_formula += sum(nums)
end = time.time()

print(sum_formula, end-start)


# 再帰関数
def calc_all_formula(S, i, lists):
    '''
    listsの要素: ([数字list], temp_str)
    '''
    new_lists = []
    # i - i+1番目の間に+が入る
    new_lists.extend(
        [(lst[0]+[int(lst[1])], S[i+1]) for lst in lists]
    )
    new_lists.extend(
        [(lst[0], lst[1]+S[i+1]) for lst in lists]
    )

    # base case
    if i == len(S)-2:
        new_lists = [
            lst[0]+[int(lst[1])] for lst in new_lists
        ]
        return new_lists
    
    return calc_all_formula(S, i+1, new_lists)

start = time.time()
base_cand = [([], S[0])]
if len(S) >= 2:
    sum_formula = sum([sum(lst) for lst in calc_all_formula(S, 0, base_cand)])
    end = time.time()
    print(sum_formula, end-start)
else:
    print(int(S))