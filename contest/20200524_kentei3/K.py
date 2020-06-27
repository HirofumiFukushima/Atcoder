# -*- coding: utf-8 -*-

def Container():
    def __init__(self, index):
        self.index = index
        self.connected_to = None

    def change_connect(self, container):
        self.connected_to = container

def Table():
    def __init__(self, index):
        self.index = index
        self.connect_to = None
    
    def change_connect(self, container):
        self.connect_to = container

N, Q = map(int, input().split())

query_list = []
for q in range(Q):
    query_list.append(list(map(int, input().split())))

containers = {n:Container(n) for n in range(1,N+1)}
tables = {n:Container(n) for n in range()}