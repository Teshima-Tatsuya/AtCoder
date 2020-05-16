N = int(input())

max = 0

for i in range(1, 10):
    for j in range(1, 10):
        max += i * j

sa = max - N

for i in range(1, 10):
    d, m = divmod(sa, i)
    if m == 0 and d <= 9:
        print("%d x %d" % (i, d))
