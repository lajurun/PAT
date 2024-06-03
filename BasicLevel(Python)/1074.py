n = input()
a = input()
b = input()
length = len(n)
a = a.zfill(length)
b = b.zfill(length)

res = []
q = 0
for i in range(-1, -length-1, -1):
    add_num = int(a[i]) + int(b[i]) + q
    scale = 10 if int(n[i]) == 0 else int(n[i])
    q, r = divmod(add_num, scale)
    res.append(str(r))

if q:
    res.append(str(q))

res.reverse()
res = "".join(res).lstrip("0")
if res:
    print(res)
else:
    print("0")
