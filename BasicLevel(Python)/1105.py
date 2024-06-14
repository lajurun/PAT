import sys


def extract(start, dct):
    res = []
    while start != "-1":
        address, data, nxt = start, *dct[start]
        res.append([address, data, nxt])
        start = nxt
    return res


def handle(l1, l2):
    res = []
    length = len(l2)
    e = 0
    for i in range(length):
        e = 2 * i + 1
        l1[e][2] = l2[i][0]
        try:
            l2[i][2] = l1[e+1][0]
        except:
            l2[i][2] = "-1"
        res.append(l1[e-1])
        res.append(l1[e])
        res.append(l2[i])
    res.extend(l1[e+1:])
    return res


start1, start2, num = sys.stdin.readline().split()
num = int(num)

all_data = {}
for i in range(num):
    address, data, nxt = sys.stdin.readline().split()
    all_data[address] = [data, nxt]

l1 = extract(start1, all_data)
l2 = extract(start2, all_data)

max_list = []
min_list = []
if len(l1) > len(l2):
    max_list = l1
    min_list = l2
else:
    max_list = l2
    min_list = l1
min_list.reverse()

res = handle(max_list, min_list)
for i in res:
    print(*i)
