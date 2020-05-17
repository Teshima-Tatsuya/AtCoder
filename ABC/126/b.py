S = input()

YY = ["{:02d}".format(i) for i in range(100)]
MM = ["{:02d}".format(i) for i in range(1, 13)]

flag = [False, False]
result = ""

# YYMMフォーマット
if S[0:2] in YY and S[2:4] in MM:
    flag[0] = True
# MMYYフォーマット
if S[2:4] in YY and S[0:2] in MM:
    flag[1] = True

if flag[0] and flag[1]:
    print("AMBIGUOUS")
elif flag[0]:
    print("YYMM")
elif flag[1]:
    print("MMYY")
else:
    print("NA")
