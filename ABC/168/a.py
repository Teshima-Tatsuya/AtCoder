N = input()

result = ""

if N[-1] in ["2", "4", "5", "7", "9"]:
    result = "hon"
elif N[-1] in ["0", "1", "6", "8"]:
    result = "pon"
else:
    result = "bon"

print(result)
