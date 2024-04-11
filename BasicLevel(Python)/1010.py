lst = list(map(int, input().split()))
lst1 = []

if len(lst) == 2 and lst[1] == 0:
    print("0 0")
else:
    for i in range(0, len(lst), 2):
        if lst[i+1] != 0:
            lst1.append(lst[i] * lst[i+1])
            lst1.append(lst[i+1] - 1)

    print(*lst1)
