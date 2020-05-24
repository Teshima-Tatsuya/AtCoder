def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N = ii()

a = 1
while True:
    if a > N:
        break
    else:
        a *= 2
print(int(a / 2))
