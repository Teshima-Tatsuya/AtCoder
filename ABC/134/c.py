import copy

N = int(input())

A = [int(input()) for i in range(N)]

B = copy.copy(A)
B.sort()

for i in range(N):
    if A[i] == B[-1]:
        print(B[-2])
    else:
        print(B[-1])
