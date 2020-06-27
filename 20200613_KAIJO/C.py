# -*- coding: utf-8 -*-
import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))

light_intensity = np.array(A)

for k in range(K):
    new_light_intensity = np.zeros(N)
    # 累積和で求める
    for i in range(N):
        left = max(0, i-light_intensity[i])
        right = min(i+light_intensity[i], N)
        new_light_intensity[left] += 1
        if right+1 < N:
            new_light_intensity[right+1] -= 1
    
    light_intensity = np.cumsum(new_light_intensity)
    
    if k > 45:
        print(" ".join(map(str, light_intensitybb)))
        exit(0)

print(" ".join(map(str, light_intensity)))