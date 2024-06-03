n = int(input())
d = {"A": "1", "B": "2", "C": "3", "D": "4"}
res = []
for _ in range(n):
    s = input()
    index = s.find("T")
    res.append(d[s[index-2]])
print("".join(res))
