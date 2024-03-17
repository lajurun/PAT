start, n, k = input().split()
n = int(n)
k = int(k)

all_data_input = []

for i in range(n):
    address, data, next = input().split()
    all_data_input.append([address, data, next])


def st(begin, lst):
    res = []
    for _ in range(n):
        for tmp in lst:
            if tmp[0] == begin:
                res.append(tmp)
                begin = tmp[2]
                break
    return res


all_data_sort = st(start, all_data_input)

all_data = []

if k == 1:
    all_data = all_data_sort
else:
    for i in range(0, n, k):
        if i + k <= n:
            tmp = all_data_sort[i:i + k]
            tmp.reverse()
            for i in tmp:
                all_data.append(i)
        else:
            for i in all_data_sort[i:]:
                all_data.append(i)

    for i in range(n - 1):
        all_data[i][2] = all_data[i + 1][0]

    all_data[n - 1][2] = -1

for i in all_data:
    print(*i)