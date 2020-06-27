# -*- coding: utf-8 -*-
# 1:49 -> 2:13, WA:1 (29min.)
import collections

H, W = map(int, input().split())

C = []
for h in range(H):
    C_h = list(input())
    if 's' in C_h:
        start = (h, C_h.index('s'))
    C.append(C_h)
is_passed = [[False for w in range(W)] for h in range(H)]

search_stack = collections.deque([start])

while len(search_stack) != 0:
    search = search_stack.pop()
    if not is_passed[search[0]][search[1]]:
        # 書かれているものは何
        if C[search[0]][search[1]] == 'g':
            print('Yes')
            exit(0)
        elif C[search[0]][search[1]] == '#':
            continue
        else:
            is_passed[search[0]][search[1]] = True
            new_search = []
            if search[0]+1 < H:
                new_search.append((search[0]+1, search[1]  ))
            if search[0]-1 >= 0:
                new_search.append((search[0]-1, search[1]  ))
            if search[1]+1 < W:
                new_search.append((search[0]  , search[1]+1))
            if search[1]-1 >= 0:
                new_search.append((search[0]  , search[1]-1))

            search_stack.extend(new_search)

print('No')