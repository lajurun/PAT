n = int(input())
l = list(map(int, input().split()))
l.sort()

num = (l[0] + l[1]) / 2
for i in range(2, n):
    num = (num + l[i]) / 2

print(int(num))
