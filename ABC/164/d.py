S = input()

result = []

for i in range(len(S) - 3):
    for j in range(i + 3, len(S)):
        if int(S[i:j+1]) % 2019 == 0:
            result.append([i + 1, j + 1])

print(len(result))
