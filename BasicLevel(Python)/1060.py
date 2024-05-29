n = int(input())
l = [int(x) for x in input().split()]
l.sort()

if l[0] > n:
    print(n)
else:
    for i in range(n-1):
        k = n - i - 1
        if l[i+1] > k:
            print(k)
            break
    else:
        print(0)
