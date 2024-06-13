def isprime(num):
    if num <= 1:
        return False
    sqt = int(num ** 0.5)
    for i in range(2, sqt + 1):
        if num % i == 0:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def add_num(num):
    sums = 0
    while num:
        sums += num % 10
        num = num // 10
    return sums


def n_nums(m):
    n_set = set()
    for i in range(1, 91):
        g = gcd(i, m)
        if g > 2 and isprime(g):
            n_set.add(i)
    return n_set


def dfs(num, rm, step, res, max_step):
    if (max_step - step) * 9 < rm:
        return
    if rm < 0:
        return
    if step == max_step:
        if rm == 0:
            num = num * 100 + 99
            if add_num(num) == m:
                n = add_num(num + 1)
                if n in ns:
                    res.append((n, num))
        return
    for i in range(10):
        num = num * 10 + i
        dfs(num, rm - i, step + 1, res, max_step)
        num //= 10


n = int(input())
for i in range(n):
    print("Case {}".format(i + 1))
    k, m = map(int, input().split())

    if k * 9 <= m:
        print("No Solution")
        continue

    ns = n_nums(m)
    if not n_nums:
        print("No Solution")
        continue

    res = []
    max_step = k - 3
    for i in range(1, 10):
        dfs(i, m - 18 - i, 0, res, max_step)

    if res:
        res.sort()
        for i in res:
            print(*i)
    else:
        print("No Solution")
