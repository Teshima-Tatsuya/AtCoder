import itertools
from operator import add

def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())
def lim(N):
    return [int(input()) for i in range(N)]

N, M, X = mi()
C = []
A = []
for i in range(N):
    CA = li()
    C.append(CA[0])
    A.append(CA[1:])

Cost = 10 ** 8
for i in range(1, N + 1):
    # 組み合わせを作成する。
    it = itertools.combinations(range(N) ,i)

    # 組み合わせに対しての理解度を合計し、それぞれMを超えているのかを確認する。
    for i in it:
        rikaido = [0] * M
        cur_cost = 0
        for j in i:
            rikaido = list(map(add, rikaido, A[j]))
            cur_cost += C[j]

            rikaiflag = True
            for k in range(M):
                if rikaido[k] < X:
                    rikaiflag = False
                    break
            if rikaiflag:
                Cost = min(Cost,cur_cost)

if Cost == 10 ** 8:
    print(-1)
else:
    print(Cost)