begin = input()
end = input()


def func(s):
    res = []
    for i in s:
        if i.isalpha():
            if i.upper() in res:
                continue
            else:
                res.append(i.upper())
        else:
            if i in res:
                continue
            else:
                res.append(i)

    return res


begin_list = func(begin)
end_list = func(end)

for i in end_list:
    begin_list.remove(i)

print("".join(begin_list))
