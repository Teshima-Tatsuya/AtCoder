N, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)

filteredA = list(filter(lambda x: x >= (sumA / (4*M)), A))

if M <= len(filteredA):
    print('Yes')
else:
    print("No")
