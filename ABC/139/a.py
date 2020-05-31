S = input()
T = input()

hit = 0
for i in range(len(S)):
    if S[i] == T[i]:
        hit += 1

print(hit)