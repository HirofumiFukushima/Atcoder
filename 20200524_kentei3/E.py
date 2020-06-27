# -*- coding: utf-8 -*-

class Node():
    def __init__(self,index):
        self.index = index
        self.rinsetsu = []
        self.color = None
    
    def add_rinsetsu(self, node):
        self.rinsetsu.append(node)
    
    def change_color(self, color):
        self.color = color
    
    def show_rinsetsu_node(self):
        print([node.index for node in self.rinsetsu])


N, M, Q = map(int, input().split())
node_dict = {n:Node(n) for n in range(1, N+1)}
# 辺の追加
for m in range(M):
    u, v = map(int, input().split())
    node_dict[u].add_rinsetsu(node_dict[v])
    node_dict[v].add_rinsetsu(node_dict[u])
# 色の設定
colors = list(map(int, input().split()))
for n in range(1,N+1):
    node_dict[n].change_color(colors[n-1])
# クエリ
query_list = []
for q in range(Q):
    query_list.append(list(map(int, input().split())))

# クエリ実行
for query in query_list:
    if query[0] == 1:
        x = query[1]
        print(node_dict[x].color)
        for node in node_dict[x].rinsetsu:
            node.change_color(node_dict[x].color)
    
    else:
        x = query[1]
        y = query[2]
        print(node_dict[x].color)
        node_dict[x].change_color(y)