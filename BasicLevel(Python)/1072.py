n, m = map(int, input().split())
m_set = set(input().split())

num = count = 0
for i in range(n):
    l = input().split()
    res = []
    for i in l[1:]:
        if i in m_set:
            res.append(i)
            count += 1
    if res:
        num += 1
        res.insert(0, l[0]+":")
        print(*res)
print(num, count)
