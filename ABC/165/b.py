X = int(input())

money = 100
year = 0
while money < X:
    money = int(money * 1.01)
    year += 1

print(year)