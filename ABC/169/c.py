from decimal import Decimal

A, B = input().split()

A = int(A)
B = Decimal(B)

print(int(A * B))
