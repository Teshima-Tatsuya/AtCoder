def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N, A, B = mi()

S = input()
oversea = 0
passes = 0

for i in range(len(S)):
    if S[i] == "a":
        if passes < (A + B):
            print("Yes")
            passes += 1
        else:
            print("No")
    elif S[i] == "b":
        oversea += 1
        if passes < (A + B) and oversea <= B:
            print("Yes")
            passes += 1
        else:
            print("No")
    else:
        print("No")
