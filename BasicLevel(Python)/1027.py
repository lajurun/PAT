num, s = input().split()

num = int(num)
res = 0

for i in range(1, num+2):
    tmp = i * (2*i-1) + (i-1)
    if tmp > num:
        res = i-1
        break

remain = num - (res * (2*res-1) + (res-1))
index = 2 * res - 1
count = index // 2

for i in range(-count, count+1):
    s0 = " " * ((index-(2*abs(i))) // 2)
    st = s * (2*abs(i)+1)
    print(s0 + st)

print(remain)
