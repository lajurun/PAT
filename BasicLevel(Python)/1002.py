n = int(input())

lst = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']

sum = 0
while n > 0:
    sum += n % 10
    n //= 10

s = ''
while sum > 0:
    i = sum % 10
    sum //= 10
    s = lst[int(i)] + ' ' + s

print(s.strip())
