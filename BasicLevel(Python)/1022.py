l = list(map(int, input().split()))

num = l[0] + l[1]
d = l[2]
res = []

if num == 0:
    print(0)
else:
    while num != 0:
        res.append(num % d)
        num //= d

    res.reverse()

    print("".join(map(str, res)))
