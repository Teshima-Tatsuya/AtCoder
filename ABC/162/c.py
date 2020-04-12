import math as f

K = int(input())
total = 0

for i in range(1, K + 1):
    for j in range(1, K + 1):
        ij = f.gcd(i, j)
        if ij == 1:
            total += K
            continue
        for k in range(1, K + 1):
            total += f.gcd(ij, k)

print(total)
