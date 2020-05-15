N = int(input())

W = []
result = "DRAW"

# 最初の単語だけ入れておく
W.append(input())

for i in range(N - 1):
    W.append(input())

    # しりとりの最後と最初の比較、および
    # 重複が無いか
    if(W[-2][-1] == W[-1][0] and len(W) == len(set(W))):
        pass
    else:
        if(i % 2 == 0):
            result = "WIN"
            break
        else:
            result = "LOSE"
            break

print(result)
