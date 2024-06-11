n = int(input())
l = [int(x) for x in input().split()]
d = {}
for i in range(len(l)):
    k = abs(l[i] - i - 1)
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

res = sorted(d.items(), reverse=True)
for i in res:
    if i[1] > 1:
        print(*i)
