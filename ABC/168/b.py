K = int(input())
S = input()

if K >= len(S):
    print(S)
else:
    ans = S[0:K] + "..."
    print(ans)
