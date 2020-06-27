# -*- coding: utf-8 -*-

N = int(input())
S = 5 # 行数

def keijiban_number(local_keijiban):
    zero_to_nine = [list(".###..#..###.###.#.#.###.###.###.###.###."),
                    list(".#.#.##....#...#.#.#.#...#.....#.#.#.#.#."),
                    list(".#.#..#..###.###.###.###.###...#.###.###."),
                    list(".#.#..#..#.....#...#...#.#.#...#.#.#...#."),
                    list(".###.###.###.###...#.###.###...#.###.###.")]

    for n in range(1,N+1):
        hikaku_num = [zero_to_nine[s][4*n-3:4*n] for s in range(S)]
        if local_keijiban == hikaku_num:
            return n-1
    
    return 9


keijiban = []
for s in range(S):
    keijiban.append(list(input()))

number_list = []
for j in range(1,N+1):
    now_keijiban = [keijiban[s][4*j-3:4*j] for s in range(S)]
    number_list.append(keijiban_number(now_keijiban))

print("".join([str(_) for _ in number_list]))