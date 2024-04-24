n, p = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
count = 0

for i in range(n):
    mp = num[i] * p
    offset = i + count
    if offset >= n:
        break
    else:
        for j in range(offset, n):
            if mp >= num[j]:
                count += 1
            else:
                break

print(count)
