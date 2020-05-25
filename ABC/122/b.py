def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


S = input()
ACGT = ["A", "C", "G", "T"]

length = 0
max_length = 0

for i in range(len(S)):
    if S[i] in ACGT:
        for j in range(i, len(S)):
            if S[j] in ACGT:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 0
                break
        max_length = max(max_length, length)
        length = 0

print(max_length)
