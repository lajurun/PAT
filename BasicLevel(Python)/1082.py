count = int(input())

i, x, y = input().split()
x, y = int(x), int(y)
n = x ** 2 + y ** 2
max_id = i
max_n = n
min_id = i
min_n =n

for _ in range(count-1):
    i, x, y = input().split()
    x, y = int(x), int(y)
    n = x ** 2 + y ** 2
    if n > max_n:
        max_n = n
        max_id = i
    if n < min_n:
        min_n = n
        min_id = i

print(min_id, max_id)
