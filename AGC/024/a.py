A, B, C, K = map(int, input().split())

for i in range(K):
    tmpA = B + C
    tmpB = A + C
    tmpC = A + B
    A = tmpA
    B = tmpB
    C = tmpC

if (A - B) >= 10**18:
    print("Unfair")
else:
    print(A - B)