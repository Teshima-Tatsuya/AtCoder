# https://atcoder.jp/contests/abc044/tasks/abc044_a
N = int(input())
K = int(input())
X = int(input())
Y = int(input())


def totalPrice(N, K, X, Y):
    total = 0
    for i in range(1, N + 1):
        if i <= K:
            total += X
        else:
            total += Y
    return total

print(totalPrice(N, K, X, Y))