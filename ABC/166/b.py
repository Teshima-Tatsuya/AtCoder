N, K = map(int, input().split())

result = [False] * N

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in range(len(A)):
        result[A[a] - 1] = True

print(result.count(False))
