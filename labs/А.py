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


def dp_ways(a, d_list):
    if a < 0:
        return 0
    dp = [0] * (a + 1)
    dp[0] = 1
    for d in d_list:
        for s in range(d, a + 1):
            dp[s] = (dp[s] + dp[s - d]) % MOD
    return dp[a]


from collections import Counter

s = input().strip()
l, r = s.split('=')

# Правая часть: вычисляем произведение чисел
rmas = r.split('*')
rightNumber = 1
for t in rmas:
    rightNumber *= int(t.strip())

# Левая часть: вычисляем произведение чисел и степени переменных
leftNumbers = 1
var_degrees = Counter()  # {переменная: степень}
lmas = l.split('*')
for temp in lmas:
    temp = temp.strip()
    if temp.isdigit():
        leftNumbers *= int(temp)
    else:
        var_degrees[temp] += 1

# Проверка делимости
if rightNumber % leftNumbers != 0:
    print(-1)
else:
    k = rightNumber // leftNumbers
    factors = factorint(k)  # Разложение k на простые множители
    d_list = list(var_degrees.values())  # Список степеней уникальных переменных

    # Вычисляем общее количество способов как произведение по простым
    result = 1
    for p, a in factors.items():
        ways = dp_ways(a, d_list)
        result = (result * ways) % MOD
    print(result)