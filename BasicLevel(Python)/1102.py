n = int(input())

num_no1 = []
price_no1 = []

for i in range(n):
    id, price, num = input().split()
    price = int(price)
    num = int(num)
    if not num_no1:
        num_no1 = [id, price, num]
        price_no1 = [id, price, num]
    else:
        if num > num_no1[2]:
            num_no1 = [id, price, num]
        if num * price > price_no1[1] * price_no1[2]:
            price_no1 = [id, price, num]

print("{} {}".format(num_no1[0], num_no1[2]))
print("{} {}".format(price_no1[0], price_no1[1] * price_no1[2]))
