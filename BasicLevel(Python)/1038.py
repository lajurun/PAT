n = int(input())
l = map(int, input().split())
inquire = list(map(int, input().split()))[1:]

score = {}
for i in l:
    if score.get(i):
        score[i] += 1
    else:
        score[i] = 1

res = [0] * len(inquire)
for i in range(len(inquire)):
    res[i] = score[inquire[i]] if score.get(inquire[i]) else 0

print(*res)
