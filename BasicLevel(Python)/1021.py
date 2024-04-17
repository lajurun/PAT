num = int(input())

d = {}

while num > 0:
    y = num % 10
    if y in d:
        d[y] += 1
    else:
        d[y] = 1
    num //= 10

res = sorted(d.items(), key=lambda x: x[0])

for a, b in res:
    print("{}:{}".format(a, b))
