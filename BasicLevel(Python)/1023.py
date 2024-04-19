num = list(map(int, input().split()))

d = {}

for i in range(len(num)):
    if num[i] != 0:
        d[i] = num[i]

res = ""
d0 = 0
flag = True
if 0 in d:
    d0 = d.pop(0)

for i, number in d.items():
    if flag and d0:
        res += str(i)
        tmp = d[i]
        tmp -= 1
        res += "0" * d0
        res += str(i) * tmp
        flag = False
    else:
        res += str(i) * d[i]

print(res)
