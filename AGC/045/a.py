import copy
import itertools
T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    S = input()

    p0 = [0]
    p1 = [0]
    for i in range(len(S)):
        if S[i] == "0":
            p0.append(int(A[i]))
        else:
            p1.append(int(A[i]))

    # xorのリスト
    p1xor = copy.copy(p1) 
    setp1xor = set(p1xor)
    comb = list(itertools.product([0,1],repeat=len(p1)))
    for c in comb:
        temp = 0
        for i in range(len(c)):
            if c[i] == 1:
                temp = temp ^ p1xor[i]
                if temp not in setp1xor:
                   setp1xor.add(temp)

    # xorのリスト
    p0xor = copy.copy(p0) 
    setp0xor = set(p0xor) 
    comb = list(itertools.product([0,1],repeat=len(p0)))
    for c in comb:
        temp = 0
        for i in range(len(c)):
            if c[i] == 1:
                temp = temp ^ p0xor[i]
                if temp not in setp0xor:
                    setp0xor.add(temp)

    
    flag = True
    for p in setp1xor:
        if p not in setp0xor:
            flag = False
            break
    if flag == True:
        print(0)
    else:
        print(1)
