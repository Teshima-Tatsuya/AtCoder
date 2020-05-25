def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N = ii()

X = N / 1.08

if int((int(X) * 1.08)) == N:
    print(int(X))
elif int(((int(X) + 1) * 1.08)) == N:
    print(int(X) + 1)
else:
    print(":(")
