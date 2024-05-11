import math


r1, p1, r2, p2 = list(map(float, input().split()))
a = r1 * math.cos(p1)
b = r1 * math.sin(p1)
c = r2 * math.cos(p2)
d = r2 * math.sin(p2)

m = a * c - b * d
n = a * d + c * b

m = 0 if abs(m) < 0.01 else m
n = 0 if abs(n) < 0.01 else n

if n >= 0:
    print("{:.2f}+{:.2f}i".format(m, n))
else:
    print("{:.2f}{:.2f}i".format(m, n))
