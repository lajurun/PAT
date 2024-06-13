def judge(num):
    x2 = num ** 3 - (num-1) ** 3
    x = x2 ** 0.5
    if x == int(x):
        for i in range(int(x**0.5), 1, -1):
            tmp = i ** 2 + (i-1) ** 2
            if tmp == x:
                return [num, i]
    else:
        return


m, n = map(int, input().split())

res = []
for i in range(m, n+1):
    result = judge(i)
    if result:
        res.append(result)

if res:
    for i in res:
        print(*i)
else:
    print("No Solution")
