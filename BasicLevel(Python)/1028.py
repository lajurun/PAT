n = int(input())
count = 0
low = []
high = []

for i in range(n):
    name, date = input().split()
    if date < '1814/09/06' or date > '2014/09/06':
        continue
    else:
        tmp = [name, date]
        if not low:
            low = tmp
            high = tmp
            count += 1
        else:
            if tmp[1] < low[1]:
                low = tmp
            elif tmp[1] > high[1]:
                high = tmp
            count += 1

if count:
    print("{} {} {}".format(count, low[0], high[0]))
else:
    print("0")
