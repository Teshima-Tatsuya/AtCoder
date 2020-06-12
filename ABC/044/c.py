S = input()

result = 0
result2 = 0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] != "0":
            result += 1
        else:
            result2 += 1
    else:
        if S[i] != "1":
            result += 1
        else:
            result2 += 1

print(min(result, result2))