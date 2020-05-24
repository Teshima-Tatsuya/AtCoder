A, B, C = map(int, input().split())

result = "NO"
for i in range(1, B+1):
    if C == ((i*A) % B):
        result = "YES"

print(result)
