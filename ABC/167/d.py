N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 1
L = 2
current = A[0]
visited = [0] * N
visited_loop_cnt = 1
flag = True

while L < K:
    if visited[current - 1] == 3:
        J = K - L
        J %= visited_loop_cnt
        K = L + J
    elif visited[current - 1] == 2 and flag:
        visited[current - 1] += 1
        visited_loop_cnt = 1
        flag = False
    else:
        visited[current - 1] += 1
        visited_loop_cnt += 1
    current = A[current - 1]
    L += 1

print(A[current - 1])


# 同じところに来た場合、そのループ分だけ減らす必要がある。
# 1 6 2 5 3 2 5 3 2 5
