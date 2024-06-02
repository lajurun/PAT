def extract_answer(lst):
    s = "".join(lst)
    answer = []
    i = 1
    while i < len(s):
        start = i + 1
        end = start + int(s[i])
        tmp = list(s[start:end])
        answer.append(tmp)
        i = end + 2
    return answer


def cal_wrong_answer(i, a, ra, wa):
    a_set = set(a)
    ra_set = set(ra)
    new_set = a_set.symmetric_difference(ra_set)
    for x in new_set:
        key = (i + 1, x)
        if key in wa:
            wa[key] += 1
        else:
            wa[key] = 1


def cal_score(a, sa):
    score = 0
    for i in range(len(a)):
        s = sa[i][0]
        ra = sa[i][1]
        cal_wrong_answer(i, a[i], ra, wrong_answers)
        if a[i] == ra:
            score += s
        else:
            if len(a[i]) < len(ra):
                for j in a[i]:
                    if j not in ra:
                        break
                else:
                    score += s / 2
    return score


n, m = map(int, input().split())

score_answers = []
for _ in range(m):
    lst = input().split()
    tmp = [int(lst[0])]
    tmp.append(lst[3:])
    score_answers.append(tmp)

wrong_answers = {}
for i in range(n):
    l = input().split()
    answer = extract_answer(l)
    score = cal_score(answer, score_answers)
    print("{:.1f}".format(score))

if wrong_answers:
    l = sorted(wrong_answers.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))
    max_num = l[0][1]
    for i in l:
        if i[1] == max_num:
            print("{} {}-{}".format(max_num, i[0][0], i[0][1]))
else:
    print("Too simple")
