N = int(input())

P = list(map(int,input().split()))

result = 0
current_min = 10**6
for i in range(N):
    current_min = min(current_min, P[i])
    if P[i] <= current_min:
        result += 1

print(result)