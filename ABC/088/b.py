def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N = ii()
a = li()

a.sort(reverse=True)

alice = 0
bob = 0

for i in range(len(a)):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)
