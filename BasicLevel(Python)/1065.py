n = int(input())
couple = {}
for _ in range(n):
    l = input().split()
    couple[l[0]] = l[1]
    couple[l[1]] = l[0]

m = int(input())
ids = set(input().split())
res = []
for i in ids:
    if i in couple and couple[i] in ids:
        continue
    res.append(i)
res.sort()

if res:
    print(len(res))
    print(*res)
else:
    print(0)
    