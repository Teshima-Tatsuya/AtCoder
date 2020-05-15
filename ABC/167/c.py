import numpy as np
from operator import add
import itertools
from functools import reduce


N, M, X = map(int, input().split())

result = [0] * M
CA = []
dp = [[] * N] * N

for i in range(N):
    CA.append(list(map(int, input().split())))

# ここからDP
for i in range(N):
    for j in range(N):
        dp[i][j].append(CA[j])
        filtered = filter(lambda x: x >= X, dp[i][j][1:])
        print(filtered)
        if(len(filtered) == M):
            pass

CA.sort(key=lambda x: x[0])

print(CA)

print(reduce(np.add, CA))
