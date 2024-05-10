import sys


n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
sort_lst = list(map(int, sys.stdin.readline().split()))
flag = False

for i in range(2, n):
    l1 = lst[:i]
    l1.sort()
    l1.extend(lst[i:])
    if flag:
        print("Insertion Sort")
        print(*l1)
        break
    if l1 == sort_lst: flag = True

if not flag:
    print("Merge Sort")
    tag = 1
    l2 = []
    while not flag:
        if l2 == sort_lst: flag = True
        l2 = []
        for i in range(0, n, tag):
            l2 += sorted(lst[i:i+tag])
        tag *= 2

    print(*l2)
