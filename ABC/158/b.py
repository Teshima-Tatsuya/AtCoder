def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())

N, A, B = mi()

div, mod = divmod(N, (A + B))

blue = div * A

if A >= mod:
    blue += mod
else:
    blue += A

print(blue)