n = int(input())

l = list(map(int, input().split()))

lst1, lst2 = [], []

for i in l:
    while i != 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = (3 * i + 1) // 2
        lst1.append(i)

for i in l:
    if i not in lst1:
        lst2.append(i)

print(*(sorted(lst2, reverse=True)))
