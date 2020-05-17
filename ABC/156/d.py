n, a, b = map(int, input().split())

mmod = 10**9 + 7


def comb_mod(n, r, mod=mmod):
    nume = 1
    deno = 1

    r = min(r, n - r)

    for i in range(1, r + 1):
        nume = (nume * (n + 1 - i)) % mod
        deno = (deno * i) % mod

    return (nume * pow(deno, mod - 2, mod)) % mod


result_a = comb_mod(n, a)
result_b = comb_mod(n, b)
total = (pow(2, n, mmod) - result_a - result_b - 1) % mmod

print(total)
