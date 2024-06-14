s = input()
p = input()

start_list = []

for i in range(len(s)):
    if s[i] == p[0]:
        start_list.append(i)


def func(s, p):
    global start_list
    lens = len(s)
    lenp = len(p)
    length = len(start_list)
    if lenp == 1:
        return p
    res = ""
    for x in range(length):
        i = start_list[x]
        i_next = start_list[x+1] if x < length-1 else lens
        cnt = 1
        if lens - i < lenp:
            return res
        for j in range(i+1, lens):
            if s[j] == p[cnt]:
                if cnt == 1 and j > i_next:
                    break
                cnt += 1
                if cnt == lenp:
                    tmp = s[i:j+1]
                    if not res:
                        res = tmp
                    if j - i + 1 == lenp:
                        return res
                    if len(tmp) < len(res):
                        res = tmp
                    break
    return res


print(func(s, p))
