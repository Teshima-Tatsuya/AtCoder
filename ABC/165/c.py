def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())
def lim(N):
    return [int(input()) for i in range(N)]

N, M, Q = mi()

a = []
b = []
c = []
d = []
for i in range(Q):
    abcd = li()
    a.append(abcd[0])
    b.append(abcd[1])
    c.append(abcd[2])
    d.append(abcd[3])

A = [0] * N
for i in range(Q):
    A[b[i] - 1] += c[i]

print(A)