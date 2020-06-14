from collections import Counter
N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
result = 0
c = Counter(sorted_A)
# 倍数を管理するテーブル
lendp = sorted_A[-1] + 1
dp = [0] * lendp

for a in sorted_A:
    dp[a] += 1
    if dp[a] == 1:
        b = a * 2
        while b < lendp:
            dp[b] += 2
            b += a

print(dp.count(1))
