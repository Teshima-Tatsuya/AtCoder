N, K = input().split()
D = input().split()

like = list(set([str(i) for i in range(1, 10)]) - set(D))

N_MAX = 10 ** 4
print(like)

# N + 1 から１ずつカウントアップして、嫌いな数字が含まれているかを確認
for i in range(int(N) + 1, N_MAX):
    # 数字に含まれているか確認
    for j in range(len(N)):
        if N[j] in D:
            continue
        else:
            print(i)
            break
