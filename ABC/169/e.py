N = int(input())


def median(N):
    N.sort()

    if len(N) % 2 == 0:
        return (N[len(N) / 2] + N[len(N) / 2 + 1]) / 2
    else:
        return N[(len(N) + 1) / 2]


Xl = []
for i in range(N):
    A, B = map(int, input().split())
    X = list(range(A, B + 1))
    Xl.append(X)

print(Xl)
