n, m = map(int, input().split())
score = [int(x) for x in input().split()]
right_answer = [int(x) for x in input().split()]

for _ in range(n):
    answer = [int(x) for x in input().split()]
    res = 0
    for i in range(m):
        if answer[i] == right_answer[i]:
            res += score[i]
    print(res)
    