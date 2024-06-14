n = int(input())

a, b = 0, 1
sums = 1
res = [0, 1]
while sums < n:
    sums = a + b
    res.append(sums)
    a, b = b, sums

if abs(res[-2] - n) <= abs(res[-1] - n):
    print(res[-2])
else:
    print(res[-1])
