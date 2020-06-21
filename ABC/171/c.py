import string
numbers = "0123456789"
alphabets = string.ascii_letters  # a-z+A-Zをロード
characters = numbers + alphabets


def base_cvt(value, n=2):
    result = ''
    tmp = int(value)
    while tmp >= n:
        idx = tmp % n
        if idx == 0:
            idx = 26
            tmp = int(tmp / n) - 1
        else:
            tmp = int(tmp / n)
        result = characters[idx] + result
    if tmp != 0:
        idx = tmp % n
        result = characters[idx] + result
    return result


N = int(input())

res = base_cvt(N, 26)
if res[-1] == "0":
    res = "q" * (len(res)-1)
for d in str(res):
    if d == "0":
        d = "q"
    if ord(d) >= 96:
        d = str(9 + ord(d) - 96)
    print(chr(96 + int(d)), end="")
print()
