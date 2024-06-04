n, m = map(int, input().split())

for _ in range(n):
    l = list(map(int, input().split()))
    g2 = l[0]
    res = []
    for i in l[1:]:
        if 0 <= i <= m:
            res.append(i)
    res.sort()
    del res[0]
    del res[-1]
    g1 = sum(res) / len(res)
    g = (g1 + g2) / 2
    r = 1 if g % 1 >= 0.5 else 0
    print(int(g) + r)
    