N, A, B = map(int, input().split())


def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)


result = 0
for i in range(N+1):
    s = digitSum(i)
    if A <= s and s <= B:
        result += i

print(result)
