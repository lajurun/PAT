num, w = input().split()
w = int(w)

index = len(num) - w
new_num = num[index:] + num[:index]

print("{:.2f}".format(int(new_num) / int(num)))
