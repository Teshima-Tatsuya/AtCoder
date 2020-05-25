def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N = ii()
A = li()

d = {}

for i in range(N):
    d[i + 1] = A[i]

d2 = sorted(d.items(), key=lambda x: x[1])

for i in range(N):
    print(d2[i][0], end=" ")
print()
