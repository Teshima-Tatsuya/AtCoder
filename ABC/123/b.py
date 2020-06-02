A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

sec_time = {}
sec_time["A"] = A, A % 10 if A % 10 != 0 else 10
sec_time["B"] = B, B % 10 if B % 10 != 0 else 10
sec_time["C"] = C, C % 10 if C % 10 != 0 else 10
sec_time["D"] = D, D % 10 if D % 10 != 0 else 10
sec_time["E"] = E, E % 10 if E % 10 != 0 else 10

sorted_sec_time = sorted(sec_time.items(), key=lambda x:x[1][1], reverse=True) 

result = 0
i = 0
for time in sorted_sec_time:
    result += time[1][0]
    i += 1
    if result % 10 != 0 and i != 5:
        result += 10 - result % 10
    
print(result)