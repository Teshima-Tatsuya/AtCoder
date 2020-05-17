N = int(input())

kind = {}
for i in range(N):
    S = input()

    if S not in kind:
        kind[S] = 1

print(len(kind))
