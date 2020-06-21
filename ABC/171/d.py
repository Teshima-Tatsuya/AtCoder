import collections


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
cnt = collections.Counter(A)

s = 0
for k, v in cnt.items():
    s += int(k) * v
for i in range(Q):
    BC = list(map(int, input().split()))

    if BC[0] in cnt:
        if BC[1] in cnt:
            cnt[BC[1]] += cnt[BC[0]]
            s += int(BC[1]) * cnt[BC[0]]
            s -= int(BC[0]) * cnt[BC[0]]
            del cnt[BC[0]]
        else:
            cnt[BC[1]] = cnt[BC[0]]
            s += int(BC[1]) * cnt[BC[0]]
            s -= int(BC[0]) * cnt[BC[0]]
            del cnt[BC[0]]
    print(s)
