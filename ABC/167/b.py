A, B, C, K = map(int, input().split())

result = 0

if K <= A:
    result = K
else:
    result = A
    K = K - A
    if K <= B:
        pass
    else:
        result -= K - B

print(result)
