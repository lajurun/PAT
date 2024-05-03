n = int(input())
d = {}
for _ in range(n):
    a, score = input().split()
    t = a.split("-")[0]
    t, score = int(t), int(score)
    if d.get(t):
        d[t] += score
    else:
        d[t] = score

d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(*d[0])
