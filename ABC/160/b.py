X = int(input())

res = 0

X500, mod = divmod(X, 500)
X5 = mod // 5

res = X500 * 1000 + X5 * 5

print(res)
