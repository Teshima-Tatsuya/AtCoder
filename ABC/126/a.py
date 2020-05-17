N, K = map(int, input().split())
S = input()

result = ""

for i in range(N):
    if i == K - 1:
        result += S[i].lower()
    else:
        result += S[i]

print(result)
