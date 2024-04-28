n, c = input().split()
n = int(n)

h = n // 2 if n % 2 == 0 else n // 2 + 1

print(c * n)
for i in range(h-2):
    print(c + " " * (n-2) + c)
print(c * n)
