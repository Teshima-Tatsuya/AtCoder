N, R = map(int, input().split())

if N >= 10:
    rate = R
else:
    rate = R + (100 * (10 - N))

print(rate)
