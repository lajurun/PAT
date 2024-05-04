import decimal


n = int(input())
l = [decimal.Decimal(i) for i in input().split()]

res = decimal.Decimal(0)
for i in range(n):
    res += l[i] * (i+1) * (n-i)

print("{:.2f}".format(res))
