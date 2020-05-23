import itertools

MOD = 1000000007

N = int(input())

AB = []
for i in range(N):
    AB.append(list(map(int, input().split())))

for i in range(1, N + 1):
    print(list(itertools.combinations(AB, i)))
