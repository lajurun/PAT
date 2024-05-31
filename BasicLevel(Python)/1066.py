def handle(lst, a, b, v):
    res = []
    for i in lst:
        if a <= i <= b:
            i = v
        tmp = "{:0>3}".format(i)
        res.append(tmp)
    return res


l = [int(x) for x in input().split()]
m, _, a, b, v = l

for _ in range(m):
    l = [int(x) for x in input().split()]
    res = handle(l, a, b, v)
    print(*res)
    