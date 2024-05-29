d = {chr(i): (i-96) for i in range(97, 123)}

s = input()
num = 0
for i in s:
    if i.isalpha():
        num += d[i.lower()]

if num != 0:
    res = bin(num)[2:]
    print(res.count('0'), res.count('1'))
else:
    print(0, 0)
