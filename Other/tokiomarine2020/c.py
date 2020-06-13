import numpy as np
from numba import njit
N, K = map(int, input().split())
A = np.array(list(map(int, input().split())), dtype=np.int64)


@njit
def solve(N, K, A):
    for i in range(K):
        # j番目の電球を操作
        B = np.zeros(N + 1, dtype=np.int64)
        for j in range(N):
            # 左辺を確認
            B[max(j - A[j], 0)] += 1
            # 右辺を確認(累積和を求めるために終端を-1とする)
            B[min(j + A[j] + 1, N)] -= 1

        # cumsumで累積和を取り、終端だけは余計なので取得しない
        A = np.cumsum(B)[:-1]

        # 全部がNならば、収束しているため終了
        if np.all(A == N):
            return A

    else:
        # 全部がNにならずループが終了した場合も:終了
        return A


A = solve(N, K, A)
for i in range(N):
    if i != (N - 1):
        print(A[i], end=" ")
    else:
        print(A[i])
