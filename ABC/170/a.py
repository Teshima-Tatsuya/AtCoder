x = list(map(int, input().split()))

for i, x_ in enumerate(x):
    if x_ == 0:
        print(i + 1)
        break
