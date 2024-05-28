def judge(s, e, d):
    s = s.split()
    k = int(s[0])
    l = [float(x) for x in s[1:]]
    count = 0
    for i in l:
        if i < e:
            count += 1
    if count >= k // 2 + 1:
        if k <= d:
            return 1
        else:
            return 2
    else:
        return 0


l = input().split()
n, e, d = int(l[0]), float(l[1]), int(l[2])
res1 = res2 = 0
for i in range(n):
    res = judge(input(), e, d)
    if res == 1:
        res1 += 1
    if res == 2:
        res2 += 1

print("{:.1%} {:.1%}".format(res1 / n, res2 / n))
