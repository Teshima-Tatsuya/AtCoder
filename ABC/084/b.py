import re

def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())
def lim(N):
    return [int(input()) for i in range(N)]

A, B = mi()
S = input()

pattern = "[0-9]+"
c = re.compile(pattern)

if c.match(S[:A]) and S[A:A+1] == "-" and c.match(S[A+1:A+1+B]):
    print("Yes")
else:
    print("No")