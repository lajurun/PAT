import sys


start, n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)

all_data = {}
for _ in range(n):
    adr, d, nt = sys.stdin.readline().split()
    all_data[adr] = (int(d), nt)

sort_data = []
while start != "-1":
    tmp = all_data[start]
    sort_data.append([start, tmp[0], tmp[1]])
    start = tmp[1]

l1 = []
l2 = []
l3 = []
for i in sort_data:
    if i[1] < 0:
        l1.append(i)
    elif i[1] <= k:
        l2.append(i)
    else:
        l3.append(i)

res = l1 + l2 + l3
for i in range(len(res) - 1):
    res[i][2] = res[i+1][0]
res[-1][2] = "-1"

for i in res:
    print(*i)
