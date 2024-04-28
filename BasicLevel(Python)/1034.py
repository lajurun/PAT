s1, s2 = input().split()
a1, b1 = map(int, s1.split("/"))
a2, b2 = map(int, s2.split("/"))


def gcd(a, b):
    a, b = (a, b) if a > b else (b, a)
    while b:
        a, b = b, a % b
    return a


def fmt(n, d):
    if n == 0:
        return "0"
    tag = True if n * d > 0 else False
    n, d = abs(n), abs(d)
    n, d = n // gcd(n, d), d // gcd(n, d)
    quotient = abs(n) // d
    remainder = abs(n) % d
    if quotient == 0:
        return "{}/{}".format(n, d) if tag else "(-{}/{})".format(n, d)
    else:
        if tag:
            return "{} {}/{}".format(quotient, remainder, d) if remainder != 0 else "{}".format(quotient)
        else:
            return "(-{} {}/{})".format(quotient, remainder, d) if remainder != 0 else "(-{})".format(quotient)


res1 = fmt(a1, b1)
res2 = fmt(a2, b2)
res_add = fmt(a1 * b2 + a2 * b1, b1 * b2)
res_subtract = fmt(a1 * b2 - a2 * b1, b1 * b2)
res_multiply = fmt(a1 * a2, b1 * b2)
res_division = "Inf" if res2 == "0" else fmt(a1 * b2, b1 * a2)
print("{} + {} = {}".format(res1, res2, res_add))
print("{} - {} = {}".format(res1, res2, res_subtract))
print("{} * {} = {}".format(res1, res2, res_multiply))
print("{} / {} = {}".format(res1, res2, res_division))
