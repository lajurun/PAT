a, b, c, d = input(), input(), input(), input()

week = {"A": "MON", "B": "TUE", "C": "WED", "D": "THU", "E": "FRI", "F": "SAT", "G": "SUN"}
tmp = 0
w = h = m = ""

for i in range(min(len(a), len(b))):
    if a[i] == b[i] and a[i] in week:
        w = week[a[i]]
        tmp = i
        break

for i in range(tmp+1, min(len(a), len(b))):
    if a[i] == b[i]:
        if "A" <= a[i] <= "N":
            h = ord(a[i]) - ord("A") + 10
            break
        elif "0" <= a[i] <= "9":
            h = ord(a[i]) - ord("0")
            break

for i in range(min(len(c), len(d))):
    if c[i] == d[i] and c[i].isalpha():
        m = i
        break

print("{} {:02}:{:02}".format(w, h, m))
