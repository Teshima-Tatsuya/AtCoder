from functools import reduce


def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N = ii()
v = li()

v.sort()


res = reduce(lambda v1, v2: (v1 + v2) / 2, v)

print(res)
