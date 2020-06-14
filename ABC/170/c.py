X, N = map(int, input().split())
p = set(map(int, input().split()))

if N == 0:
    print(X)
else:
    for i in range(100):
        # 左からと右からを交互に計算
        left = X - i
        right = X + i

        if left not in p:
            print(left)
            break
        if right not in p:
            print(right)
            break
