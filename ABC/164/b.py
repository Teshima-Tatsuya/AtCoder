A, B, C, D = map(int, input().split())

turn = 1
while True:

    # 高橋くん
    if turn % 2 != 0:
        C = C - B
        pass
    # 青木くん
    else:
        A = A - D
        pass

    if A <= 0 or C <= 0:
        break
    turn += 1

if turn % 2 != 0:
    print("Yes")
else:
    print("No")
