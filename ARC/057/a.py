A, K = map(int, input().split())

target = 2 * 10 ** 12

now = A
days = 0

if K == 0:
    days = target - A
else:
    while now < target:
        now += 1 + K * now
        days += 1

print(days)
