s = input()
d = {"P": s.count("P"),
     "A": s.count("A"),
     "T": s.count("T"),
     "e": s.count("e"),
     "s": s.count("s"),
     "t": s.count("t")}

res = ""
for _ in range(max(d.values())):
    for i in d:
        if d[i] > 0:
            res += i
            d[i] -= 1

print(res)
