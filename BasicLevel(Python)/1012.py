l = list(map(int, input().split()))
del l[0]

lst = [[], [], [], [], []]

for i in l:
    remainder = i % 5
    match remainder:
        case 0 if i % 2 == 0:
            lst[0].append(i)
        case 1:
            lst[1].append(i)
        case 2:
            lst[2].append(i)
        case 3:
            lst[3].append(i)
        case 4:
            lst[4].append(i)

lst1 = []
for i in range(5):
    num = 0
    if lst[i]:
        match i:
            case 0:
                num = sum(lst[i])
            case 1:
                for j in range(len(lst[i])):
                    num += (-1)**j * lst[i][j]
            case 2:
                num = len(lst[i])
            case 3:
                num = round(sum(lst[i]) / len(lst[i]), 1)
            case 4:
                num = max(lst[i])
        lst1.append(num)
    else:
        lst1.append("N")

print(*lst1)
