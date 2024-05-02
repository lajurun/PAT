n = int(input())
l = list(map(int, input().split()))

res = []
max_num = 0
l_sort = sorted(l)
for i in range(n):
    if l[i] < max_num:
        continue
    else:
        max_num = l[i]
        if l_sort[i] == max_num:
            res.append(l[i])

res = sorted(res)
print(len(res))
print(*res)
