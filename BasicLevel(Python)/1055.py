def print_custom(lst, m):
    res = [" "] * m
    index = m // 2
    for i in range(m):
        index += i * (-1) ** i
        res[index] = lst[i][0]
    print(*res)


n, k = map(int, input().split())

l = []
for _ in range(n):
    tmp = input().split()
    l.append([tmp[0], int(tmp[1])])

l_sort = sorted(l, key=lambda x: (-x[1], x[0]))
q, r = divmod(n, k)
index = q + r
print_custom(l_sort[:index], q + r)
while index < n:
    print_custom(l_sort[index:index+q], q)
    index += q
