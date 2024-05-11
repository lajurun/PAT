count = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

count_sqrt = int(count ** 0.5)
m, n = 0, 0
for i in range(count_sqrt, 0, -1):
    if count % i == 0:
        m, n = count // i, i
        break

res = []
for i in range(m):
    res.append([0] * n)

row_end, col_end = m, n
row_start, col_start = 0, 0
tag = 0
i, j = 0, 0
while tag < count:
    for j in range(col_start, col_end):
        res[i][j] = lst[tag]
        tag += 1
    if tag >= count:
        break

    for i in range(row_start + 1, row_end):
        res[i][j] = lst[tag]
        tag += 1
    if tag >= count:
        break
    col_end -= 1

    for j in range(col_end - 1, col_start - 1, -1):
        res[i][j] = lst[tag]
        tag += 1
    if tag >= count:
        break
    row_end -= 1

    for i in range(row_end - 1, row_start, -1):
        res[i][j] = lst[tag]
        tag += 1
    if tag >= count:
        break
    row_start = i
    col_start = j + 1

for l in res:
    print(*l)
