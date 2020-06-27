# -*- coding: utf-8 -*-
# 2:47-3:16(WA:1) -> 34min
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.friends = []

    def add_friends(self, node):
        self.friends.append(node)

    def create_friends_idx_set(self):
        self.friends_set = set([node.idx for node in self.friends])
    
    def is_all_friend(self, idx_set):
        return idx_set <= (self.friends_set | set([self.idx]))

N, M = map(int, input().split())

nodes = []
for i in range(N):
    new_node = Node(i+1)
    nodes.append(new_node)
for j in range(M):
    x_j, y_j = map(int, input().split())
    nodes[x_j-1].add_friends(nodes[y_j-1])
    nodes[y_j-1].add_friends(nodes[x_j-1])
for node in nodes:
    node.create_friends_idx_set()

max_habatsu = 0
for bit in range(2**N):
    idx_set = set()
    for shift in range(N):
        if (bit>>shift)&1:
            idx_set.add(shift+1)
    for idx in idx_set:
        if not nodes[idx-1].is_all_friend(idx_set):
            break
    else:
        max_habatsu = max(max_habatsu, len(idx_set))

print(max_habatsu)