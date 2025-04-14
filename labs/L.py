MOD = 10 ** 9 + 7


def factorint(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def comb(n, k):
    if k < 0 or k > n:
        return 0

    num = den = 1
    for i in range(k):
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD

    def mod_inverse(a, m):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        _, x, _ = extended_gcd(a, m)
        return (x % m + m) % m

    return (num * mod_inverse(den, MOD)) % MOD


s = input().strip()
l, r = s.split('=')

rmas = r.split('*')
rightNumber = 1
for t in rmas:
    rightNumber *= int(t.strip())

peremenaa = []
leftNumbers = 1
lmas = l.split('*')
for temp in lmas:
    temp = temp.strip()
    if temp.isdigit():
        leftNumbers *= int(temp)
    else:
        peremenaa.append(temp)

if leftNumbers == 0:
    print(-1)
    exit()
if leftNumbers > rightNumber:
    print(-1)
    exit()
if leftNumbers == rightNumber:
    print(1)
    exit()

k = rightNumber // leftNumbers
if k * leftNumbers != rightNumber:
    print(-1)
    exit()

factors = factorint(k)
l_len = len(peremenaa)

result = 1
for p, a in factors.items():
    ways = comb(a + l_len - 1, l_len - 1)
    result = (result * ways) % MOD

print(result)
