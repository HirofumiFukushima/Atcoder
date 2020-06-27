# -*- coding: utf-8 -*-

H1, M1, H2, M2, K = map(int, input().split())

print(max((H2*60+M2) - (H1*60+M1) - K, 0))