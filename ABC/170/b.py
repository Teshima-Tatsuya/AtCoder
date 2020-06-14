X, Y = map(int, input().split())

# すべて鶴だと仮定する
turu = X

asi = turu * 2

if asi > Y or (Y % 2) != 0 or X * 4 < Y:
    print("No")
else:
    husoku = Y - asi

    kame = husoku // 2

    turu = turu - kame

    if turu * 2 + kame * 4 == Y:
        print("Yes")
    else:
        print("No")
