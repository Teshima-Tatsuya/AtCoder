A, B, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 割引券を使用しない
result = min(a) + min(b)

# 割引券を使用する
for i in range(M):
    x, y, c = map(int,input().split())
    result = min(result, a[x-1]+b[y-1] -c)

print(result)