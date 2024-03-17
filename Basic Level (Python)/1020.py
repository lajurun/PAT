n, d = list(map(int, input().split()))
l1 = list(map(float, input().split()))
l2 = list(map(float, input().split()))

l = []
for i in range(n):
    if l1[i] != 0:
        l.append([l2[i] / l1[i], l1[i], l2[i]])

l.sort(key=lambda x: x[0], reverse=True)

sum = 0

for i in l:
    a, b, c = i[0], i[1], i[2]
    if d <= 0:
        break
    elif d >= b:
        sum += a * b
        d -= b
    else:
        sum += a * d
        d = 0

print("{:.2f}".format(sum))
