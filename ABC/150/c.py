import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

S = []
for i in range(N):
    S.append(i+1)

a = 0
b = 0
i = 1

for v in itertools.permutations(S, N):
    if list(v) == P:
        a = i
    if  list(v) == Q:
        b = i
    i += 1

print(abs(a-b))