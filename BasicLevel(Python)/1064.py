def handle(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res


n = int(input())
num_list = [int(x) for x in input().split()]
num_sum = [handle(x) for x in num_list]
res = set(num_sum)
l = sorted(res)
print(len(l))
print(*l)
