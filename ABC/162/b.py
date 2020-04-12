N = int(input())

total = 0

for i in range(N + 1):
    if i % 3 == 0 or i % 5 == 0:
        pass
    else:
        total += i

print(total)
