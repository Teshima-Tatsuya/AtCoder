def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())

N = ii()
A = li()
cnt = 0
while all(e % 2 == 0 for e in A):
    cnt += 1
    A = list(map(lambda x: x // 2, A))

print(cnt)