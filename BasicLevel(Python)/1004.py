n = int(input())

high, low = [], []

for i in range(n):
    s = input()
    lst = s.split()
    if i == 0:
        high = lst
        low = lst
    else:
        if int(lst[2]) > int(high[2]):
            high = lst
        if int(lst[2]) < int(low[2]):
            low = lst

print(high[0] + " " + high[1])
print(low[0] + " " + low[1])
