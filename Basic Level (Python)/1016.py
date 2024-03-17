l = list(map(int, input().split()))

l1 = l[:2]
l2 = l[2:]
s1 = str(l1[0])
t1 = str(l1[1])
s2 = str(l2[0])
t2 = str(l2[1])
n1 = s1.count(t1)
n2 = s2.count(t2)


def f(t, n):
    count = 1
    sum = 0
    for i in range(int(n)):
        sum += count * int(t)
        count *= 10
    return sum


print(f(t1, n1) + f(t2, n2))
