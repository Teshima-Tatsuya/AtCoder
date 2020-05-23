import math

A, B, H, M = map(int, input().split())

Atheta = H * 30 + 0.5*M
Btheta = M * 6

theta = min(abs(Atheta - Btheta), abs(360 - (Atheta - Btheta)))

C = math.sqrt(pow(A, 2) + pow(B, 2) - 2 * A*B*math.cos(math.radians(theta)))
print(C)
