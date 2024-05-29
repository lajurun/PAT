l = [int(x) for x in input().split()]
l = l[1:]

num = 0
for i in l:
    num += i * 10 + i

print(num * (len(l) - 1))
