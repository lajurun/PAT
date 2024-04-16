n = int(input())

dct_j = {"win": 0, "tie": 0, "lose": 0}
dct_y = {"win": 0, "tie": 0, "lose": 0}
win_j = {"B": 0, "C": 0, "J": 0}
win_y = {"B": 0, "C": 0, "J": 0}

for i in range(n):
    lst = input().split()
    match lst:
        case ["B", "B"] | ["C", "C"] | ["J", "J"]:
            dct_j["tie"] += 1
            dct_y["tie"] += 1
        case ["B", "C"]:
            dct_j["win"] += 1
            dct_y["lose"] += 1
            win_j["B"] += 1
        case ["B", "J"]:
            dct_j["lose"] += 1
            dct_y["win"] += 1
            win_y["J"] += 1
        case ["C", "B"]:
            dct_j["lose"] += 1
            dct_y["win"] += 1
            win_y["B"] += 1
        case ["C", "J"]:
            dct_j["win"] += 1
            dct_y["lose"] += 1
            win_j["C"] += 1
        case ["J", "B"]:
            dct_j["win"] += 1
            dct_y["lose"] += 1
            win_j["J"] += 1
        case ["J", "C"]:
            dct_j["lose"] += 1
            dct_y["win"] += 1
            win_y["C"] += 1


def st(d):
    return d[1], -ord(d[0])


tmp1 = sorted(win_j.items(), key=st, reverse=True)
tmp2 = sorted(win_y.items(), key=st, reverse=True)

print(*dct_j.values())
print(*dct_y.values())
print(*(tmp1[0][0], tmp2[0][0]))
