l = list(map(int, input().split()))
del l[0]

lst = [[], [], [], [], []]
lst1 = []

for i in l:
    if i % 5 == 0 and i % 2 == 0:
        lst[0].append(i)
    elif i % 5 == 1:
        lst[1].append(i)
    elif i % 5 == 2:
        lst[2].append(i)
    elif i % 5 == 3:
        lst[3].append(i)
    elif i % 5 == 4:
        lst[4].append(i)

for i in range(5):
    num = 0
    if lst[i]:
        if i == 0:
            num = sum(lst[i])
        elif i == 1:
            for j in range(len(lst[i])):
                num += (-1)**j * lst[i][j]
        elif i == 2:
            num = len(lst[i])
        elif i == 3:
            num = round(sum(lst[i]) / len(lst[i]), 1)
        elif i == 4:
            num = max(lst[i])
        lst1.append(num)
    else:
        lst1.append("N")

print(*lst1)