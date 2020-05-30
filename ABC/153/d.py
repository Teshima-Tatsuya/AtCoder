H = int(input())


# 2 or 3が残った場合は、3回必要

leaf = 1
while H >= 1:
    H /= 2
    leaf *= 2

print(leaf - 1)