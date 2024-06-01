m, n, s = map(int, input().split())
s -= 1
l = []
for _ in range(m):
    l.append(input())

check = set()
while s < m:
    if l[s] not in check:
        print(l[s])
        check.add(l[s])
        s += n
    else:
        s += 1

if not check:
    print("Keep going...")
    