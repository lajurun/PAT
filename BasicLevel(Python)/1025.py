start, n, k = input().split()
n, k = int(n), int(k)

data_input = {}
for i in range(n):
    address, data, next_address = input().split()
    data_input[address] = (data, next_address)


def st(dct, begin):
    res = []
    n = len(dct)
    for _ in range(n):
        res.append([begin, *dct[begin]])
        begin = dct[begin][1]
        if begin == "-1":
            break
    return res


def ret(lst, k):
    data = []
    n = len(lst)

    if k == 1:
        return lst
    else:
        for i in range(0, n, k):
            if i + k <= n:
                tmp = lst[i:i + k]
                tmp.reverse()
                data.extend(tmp)
            else:
                data.extend(lst[i:])

    for i in range(n - 1):
        data[i][2] = data[i + 1][0]
    data[n - 1][2] = "-1"

    return data


data_sort = st(data_input, start)
data_result = ret(data_sort, k)
for i in data_result:
    print(*i)
