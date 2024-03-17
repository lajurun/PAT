n, l, h = list(map(int, input().split()))
l1 = []
l2 = []
l3 = []
l4 = []

for j in range(n):
    lst = list(map(int, input().split()))

    k, d, c = lst[0], lst[1], lst[2]
    if d < l or c < l:
        continue
    elif d >= h and c >= h:
        l1.append(lst)
    elif d >= h and c < h:
        l2.append(lst)
    elif d >= c:
        l3.append(lst)
    else:
        l4.append(lst)


def st(lst):
    return -(lst[1] + lst[2]), -lst[1], lst[0]


print(len(l1) + len(l2) + len(l3) + len(l4))

for i in (l1, l2, l3, l4):
    i.sort(key=st)
    for j in i:
        print(*j)

