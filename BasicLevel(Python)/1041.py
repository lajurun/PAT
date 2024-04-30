n = int(input())
d = {}
for i in range(n):
    a, b, c = input().split()
    d[b] = (a, c)

count = int(input())
l = input().split()

for i in l:
    print(*d[i])
