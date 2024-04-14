n, l, h = map(int, input().split())
l1 = []
l2 = []
l3 = []
l4 = []

for j in range(n):
    k, d, c = map(int, input().split())

    if d < l or c < l:
        continue
    elif d >= h and c >= h:
        l1.append((k, d, c))
    elif d >= h and c < h:
        l2.append((k, d, c))
    elif d >= c:
        l3.append((k, d, c))
    else:
        l4.append((k, d, c))


def st(lst):
    return -(lst[1] + lst[2]), -lst[1], lst[0]


print(len(l1) + len(l2) + len(l3) + len(l4))

for i in (l1, l2, l3, l4):
    i.sort(key=st)
    for j in i:
        print(*j)
