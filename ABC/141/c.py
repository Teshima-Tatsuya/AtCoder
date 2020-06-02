N, K, Q =map(int, input().split())

A = {}
for i in range(Q):
    a = int(input())
    if a in A:
        A[a] += 1
    else:
        A[a] = 1

for i in range(N):
    if K - Q > 0:
        print("Yes")
    elif (i + 1) in A:
        if (K - (Q -A[i + 1])) > 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")