n = int(input())
count = 0

prime_number = [2]

for i in range(3, n+1, 2):
    sqrt = i ** 0.5
    for j in prime_number:
        if i % j == 0:
            break
        elif j > sqrt:
            prime_number.append(i)
            break

for i in range(1, len(prime_number)):
    if prime_number[i] - prime_number[i-1] == 2:
        count += 1

print(count)
