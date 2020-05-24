T = int(input())

for i in range(T):
    x = 0
    coin = 0
    costs = {}
    N, A, B, C, D = map(int, input().split())
    costs["A"] = A / 15
    costs["B"] = B / 10
    costs["C"] = C / 6
    min_key = max(costs, key=costs.get)
    x = 1
    coin = D
    while (x == N) == False:
        if x < N:
            if min_key == "A":
                coin += A
                x *= A
            elif min_key == "B":
                coin += B
                x *= B
            else:
                coin += C
                x *= C
        else:
            x -= 1
            coin += D
    print(coin)
