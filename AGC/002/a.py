a, b = map(int, input().split())

# 0を挟む場合
if a <= 0 and 0 <= b:
    print("Zero")
# 両方プラスの場合
elif a > 0:
    print("Positive")
else:
    if (b + a + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")