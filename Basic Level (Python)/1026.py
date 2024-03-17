c1, c2 = map(int, input().split())

c = c2 - c1
if c < 50:
    c = 0
elif 50 <= c <100:
    c = 1
else:
    c /= 100
    c = int(c) if c % int(c) < 0.5 else int(c) + 1


def res(n):
    h = m = s = 0
    if n == 1:
        return (0, 0, 0)
    h, n = divmod(n, 3600)
    if n == 0:
        return (h, 0, 0)
    else:
        m, s = divmod(n, 60)
        return (h, m, s)


print("{:02}:{:02}:{:02}".format(*res(c)))
