import math


def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    i = n
    while True:
        if is_prime(i):
            return i
        i += 1


X = ii()

print(next_prime(X))
