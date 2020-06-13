A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if A <= B:
    maxA = A + V * T
    maxB = B + W * T
    if maxA >= maxB:
        print("YES")
    else:
        print("NO")
else:
    maxA = A - V * T
    maxB = B - W * T
    if maxA <= maxB:
        print("YES")
    else:
        print("NO")
