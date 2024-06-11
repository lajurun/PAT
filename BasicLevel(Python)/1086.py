a, b = map(int, input().split())
s = a * b
s = str(s)
res = int("".join(reversed(s)))
print(res)
