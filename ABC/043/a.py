# https://atcoder.jp/contests/abc043/tasks/abc043_a
N = int(input())

def ame(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    return total
    
print(ame(N))

