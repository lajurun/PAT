def handle(f):
    res = int(f)
    r = 1 if f % 1 >= 0.5 else 0
    res += r
    return res


p, m, n = map(int, input().split())

d = {}
for _ in range(p):
    name, score = input().split()
    d[name] = [int(score), -1, -1]

for _ in range(m):
    name, score = input().split()
    if name in d:
        d[name][1] = int(score)
    else:
        d[name] = [-1, int(score), -1]

for _ in range(n):
    name, score = input().split()
    if name in d:
        d[name][2] = int(score)
    else:
        d[name] = [-1, -1, int(score)]

res = []
for i in d:
    if d[i][0] < 200:
        continue
    if d[i][1] == -1 and d[i][2] < 60:
        continue
    if d[i][2] >= 60 and d[i][2] >= d[i][1]:
        res.append([i, d[i][0], d[i][1], d[i][2], d[i][2]])
        continue
    m = 0 if d[i][1] == -1 else d[i][1]
    f = 0 if d[i][2] == -1 else d[i][2]
    score = m * 0.4 + f * 0.6
    score = handle(score)
    if score >= 60:
        res.append([i, d[i][0], d[i][1], d[i][2], score])

l = sorted(res, key=lambda x: (-x[4], x[0]))
for i in l:
    print(*i)
