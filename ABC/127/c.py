N, M = map(int, input().split())

c_min = 1
c_max = 10 ** 5
for i in range(M):
    LM = list(map(int, input().split()))
    c_min = max(c_min, LM[0])
    c_max = min(c_max, LM[1])

if c_min > c_max:
    print(0)
else:
    print(c_max - c_min + 1)