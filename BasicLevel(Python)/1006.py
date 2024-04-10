n = int(input())

s = ""
lst = [" ", "S", "B"]
count = 0
while n > 0:
    i = n % 10

    if count == 0:
        for j in range(1, i+1):
            s = s + str(j)
    else:
        s = lst[count] * int(i) + s

    n //= 10
    count += 1

print(s)
