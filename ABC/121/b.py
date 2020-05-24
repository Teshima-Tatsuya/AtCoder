def li():
    return list(map(int, input().split()))


N, M, C = map(int, input().split())

B = li()

res = 0

for i in range(N):
    A = li()
    point = 0
    for j in range(M):
        point += A[j] * B[j]
    point += C

    if point > 0:
        res += 1

print(res)
