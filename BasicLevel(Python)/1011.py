t = int(input())

for i in range(t):
    lst = list(map(int, input().split()))
    if lst[0] + lst[1] > lst[2]:
        print("Case #{}: true".format(i+1))
    else:
        print("Case #{}: false".format(i+1))
