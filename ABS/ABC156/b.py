N, K = map(int, input().split())

keta = 0
a = N
while True:
    a = a // K
    keta = keta + 1
    if a == 0:
        break

print(keta)
