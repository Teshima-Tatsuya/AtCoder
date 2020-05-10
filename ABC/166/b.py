N, K = map(int, input().split())

result = [False] * N

for i in range(N):
    d = int(input())
    A = list(map(int, input().split()))
    for a in range(len(A)):
        result[a] = True


print(result)
