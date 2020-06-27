# -*- coding: utf-8 -*-
import copy

class Node():
    def __init__(self, index):
        self.index = index
        self.connect = []
        self.michi = None
    
    def add_edge(self, node):
        self.connect.append(node)
    
    def show_connect_node_index(self):
        return [node.index for node in self.connect]
    
    def add_michisirube(self, index):
        self.michi = index


N, M = map(int, input().split())
node_list = [Node(i) for i in range(1,N+1)]

for m in range(M):
    A_m, B_m = map(int, input().split())
    node_list[A_m-1].add_edge(node_list[B_m-1])
    node_list[B_m-1].add_edge(node_list[A_m-1])

# 道標追加。Node 1から順に
tansaku_node = [node_list[0]]
while tansaku_node != []:
    new_tansaku_node = []
    for node in tansaku_node:
        for child_node in node.connect:
            if child_node.michi == None:
                child_node.michi = node.index
                new_tansaku_node.append(child_node)
    tansaku_node = new_tansaku_node

print('Yes')
for n in range(1,N):
    print(node_list[n].michi)