def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())
def lim(N):
    return [int(input()) for i in range(N)]

N = ii()
a = lim(N)

current = 1
result = 1

for i in range(N):
    if a[current - 1] == 2:
        print(result)
        break
    else:
        current = a[current - 1]
        result += 1
else:
    print(-1)