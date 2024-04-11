n ,m = list(map(int, input().split()))
lst = list(map(int, input().split()))

if m == 0 or m == n or n == 0:
    print(*lst)
else:
    m %= n
    lst1 = lst[(len(lst)-m):] + lst[:(len(lst)-m)]
    print(*lst1)
