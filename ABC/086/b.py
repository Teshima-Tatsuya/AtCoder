import math


def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


a, b = li()

ab = str(a) + str(b)

if float.is_integer(math.sqrt(int(ab))):
    print("Yes")
else:
    print("No")
