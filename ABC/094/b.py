def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N, M, X = mi()
A = li()

filterdA = list(filter(lambda x: x <= X, A))

print(min(M - len(filterdA), len(filterdA)))
