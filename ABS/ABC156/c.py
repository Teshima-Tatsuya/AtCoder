N = int(input())
X = list(map(int, input().split()))

X.sort()

sumx = sum(X)
lenx = len(X)

point = round(sumx / lenx)

totalcost = 0
for Xi in X:
    totalcost += pow((Xi - point), 2)

print(totalcost)
