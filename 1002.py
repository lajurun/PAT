n = int(input())

lst = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
num = 0

while n > 0:
    num += n % 10
    n //= 10

s = ''
while num > 0:
    i = num % 10
    num //= 10
    s = lst[int(i)] + ' ' + s

print(s.strip())