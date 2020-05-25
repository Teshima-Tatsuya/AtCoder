def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N = ii()
d = li()

d.sort()

mean = d[len(d) // 2]

res = 0
if d[len(d) // 2 - 1] < mean:
    res = mean - d[len(d) // 2 - 1]
print(res)
