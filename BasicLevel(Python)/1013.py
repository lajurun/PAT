m, n = list(map(int, input().split()))

count = 1
prime = [2]
num = 3

while count < n:
    sqrt = num ** 0.5
    for i in prime:
        if num % i == 0:
            break
        elif i > sqrt:
            prime.append(num)
            count += 1
            break

    num += 2

lst = prime[m-1:n]

for i in range(0, len(lst), 10):
    print(*lst[i:i+10])
