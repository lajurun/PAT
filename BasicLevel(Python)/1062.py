def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


l = input().split()
k = int(l[2])
n1 = [int(x) for x in l[0].split("/")]
n2 = [int(x) for x in l[1].split("/")]
a = n1[0] * k / n1[1]
b = n2[0] * k / n2[1]
min_n = min(a, b)
max_n = max(a, b)


res = []
for i in range(int(min_n), int(max_n)+1):
    if min_n < i < max_n and gcd(k, i) == 1:
        tmp = "{}/{}".format(i, k)
        res.append(tmp)

print(*res)
