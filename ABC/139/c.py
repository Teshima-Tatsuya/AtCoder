N = int(input())
H = list(map(int, input().split()))

max_move = 0
tmp_max_move = 0
for i in range(1, N):
    if H[i] <= H[i -1]:
        tmp_max_move += 1
    else:
        max_move = max(max_move, tmp_max_move)
        tmp_max_move = 0

max_move = max(max_move, tmp_max_move)
print(max_move)