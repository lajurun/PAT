n = int(input())

j1 = [0, 0, 0]
y1 = [0, 0, 0]
j2 = {"B": 0, "C": 0, "J": 0}
y2 = {"B": 0, "C": 0, "J": 0}

for i in range(n):
    l = list(input().split())
    j = l[0]
    y = l[1]
    if j == "B":
        if y == "B":
            j1[1] += 1
            y1[1] += 1
        elif y == "C":
            j1[0] += 1
            y1[2] += 1
            j2["B"] += 1
        else:
            j1[2] += 1
            y1[0] += 1
            y2["J"] += 1
    elif j == "C":
        if y == "C":
            j1[1] += 1
            y1[1] += 1
        elif y == "J":
            j1[0] += 1
            y1[2] += 1
            j2["C"] += 1
        else:
            j1[2] += 1
            y1[0] += 1
            y2["B"] += 1
    else:
        if y == "J":
            j1[1] += 1
            y1[1] += 1
        elif y == "B":
            j1[0] += 1
            y1[2] += 1
            j2["J"] += 1
        else:
            j1[2] += 1
            y1[0] += 1
            y2["C"] += 1


def st(d):
    for k, v in d.items():
        tmp = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return tmp[0][0]


print(*j1)
print(*y1)
print(*(st(j2), st(y2)))