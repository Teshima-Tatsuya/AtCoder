K, N = map(int, input().split())

A = list(map(int, input().split()))

S = []
for i in range(1, N):
    S.append(A[i] - A[i-1])
S.append(A[0]-A[-1] + K)

print(K - max(S))
