def extract_answer(s_list):
    res = []
    s = "".join(s_list)
    i = 1
    while i < len(s):
        incre = int(s[i])
        res.append(s[i+1:i+1+incre])
        i = i + incre + 3
    return res


n, m = map(int, input().split())

score_answer = []
for _ in range(m):
    s = input().split()
    score_answer.append((int(s[0]), "".join(s[3:])))

d = {}
for _ in range(n):
    s_lst = input().split()
    answer = extract_answer(s_lst)
    score = 0
    for i in range(len(answer)):
        if answer[i] == score_answer[i][1]:
            score += score_answer[i][0]
        else:
            try:
                d[i+1] += 1
            except:
                d[i+1] = 1
    print(score)

if d:
    l = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    max_num = l[0][1]
    res = [max_num, l[0][0]]
    for i in range(1, len(l)):
        if l[i][1] == max_num:
            res.append(l[i][0])
        else:
            break
    print(*res)
else:
    print("Too simple")
    