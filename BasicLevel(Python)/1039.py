p = input()
n = input()


def s_to_d(s):
    res = {}
    for i in s:
        if res.get(i):
            res[i] += 1
        else:
            res[i] = 1
    return res


p_dict = s_to_d(p)
n_dict = s_to_d(n)
tag = True
count = 0
for i in n_dict:
    if p_dict.get(i):
        p_dict[i] = p_dict[i] - n_dict[i]
        if p_dict[i] < 0:
            tag = False
            count += abs(p_dict[i])
    else:
        tag = False
        count += n_dict[i]

if not tag:
    print("{} {}".format("No", count))
else:
    print("{} {}".format("Yes", sum(p_dict.values())))
