N, M = map(int, input().split())

A = list(map(int, input().split()))

totalA = sum(A)

ans = N - totalA

if ans < 0:
    print(-1)
else:
    print(ans)
