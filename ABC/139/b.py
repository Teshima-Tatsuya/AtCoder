A, B = map(int, input().split())

tmp = B // (A - 1)

if B == 1:
    print(0)
elif A == 2:
    print(B - 1)
elif tmp * (A - 1) + 1 >= B:
    print(tmp)
else:
    print(tmp + 1)
