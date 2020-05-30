
S = input()

result = 1000

for i in range(len(S)-2):
    X = int(S[i:i+3])
    result = min(result, abs(X - 753))

print(result)