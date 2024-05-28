n = int(input())
nums = input().split()
count = res = 0

for i in nums:
    try:
        tmp = float(i)
        if -1000.00 <= tmp <= 1000.00 and round(tmp, 2) == tmp:
            count += 1
            res += tmp
        else:
            print("ERROR: {} is not a legal number".format(i))
    except:
        print("ERROR: {} is not a legal number".format(i))

if count == 0:
    print("The average of 0 numbers is Undefined")
elif count == 1:
    print("The average of 1 number is {:.2f}".format(res))
else:
    print("The average of {} numbers is {:.2f}".format(count, res / count))
