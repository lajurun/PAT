a, b = input().split()
a, b = list(a), list(b)

if len(a) > len(b):
    b = ["0"] * (len(a) - len(b)) + b
    res = []
else:
    res = b[:(len(b)-len(a))]

for i in range(-len(a), 0):
    if abs(i) % 2 != 0:
        n = (int(a[i]) + int(b[i])) % 13
        match n:
            case 10:
                res.append("J")
            case 11:
                res.append("Q")
            case 12:
                res.append("K")
            case _:
                res.append(str(n))
    else:
        n = int(b[i]) - int(a[i])
        n = n if n >= 0 else n + 10
        res.append(str(n))

print("".join(res))
