# https://atcoder.jp/contests/abc042/tasks/abc042_b
N, L = [int(i) for i in input().split()]

S = []
for s in range(0, N):
    S.append(input())
S.sort()

print(''.join(S))