n = int(input())

max_n = 0
for _ in range(n):
    l = [int(x) for x in input().split()]
    tmp = l[0] ** 2 + l[1] ** 2
    if tmp > max_n:
        max_n = tmp

print("{:.2f}".format(max_n ** 0.5))
