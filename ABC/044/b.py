import collections

w = input()
flag = True
for v in collections.Counter(w).values():
    if v % 2 != 0:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
