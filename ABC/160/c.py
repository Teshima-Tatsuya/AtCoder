def samax_index(A):
    samax = 0
    max_i = 0
    prev_v = 0
    for i, v in enumerate(A):
        if samax <= (v - prev_v):
            max_i = i
            samax = v - prev_v
        prev_v = v
    return max_i


def distance(A, start_i, N):
    print(start_i)
    if (start_i == 0) or ((start_i + 1) == N):
        total = A[start_i] - A[1]
    else:
        total = A[start_i]
        total += A[-1] - A[start_i + 1]

    print(total)


K, N = map(int, input().split())

A = list(map(int, input().split()))
A.append(K)
A.insert(0, 0)
start_i = samax_index(A) - 1


distance(A, start_i, N)
