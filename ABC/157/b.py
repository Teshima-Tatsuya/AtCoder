# 途中
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

A = A1 + A2 + A3
N = int(input())

index = []
for i in range(N):
    inp = int(input())
    if inp in A:
        index.append(A.index(inp))

if \
   (0 in index and 3 in index and 6 in index) or \
   (1 in index and 4 in index and 7 in index) or \
   (2 in index and 5 in index and 8 in index) or \
   (0 in index and 4 in index and 8 in index) or \
   (2 in index and 4 in index and 6 in index) or \
   (0 in index and 1 in index and 2 in index) or \
   (3 in index and 4 in index and 5 in index) or \
   (6 in index and 7 in index and 8 in index):
    print("Yes")
else:
    print("No")
