low = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly","aug", "sep", "oct", "nov", "dec"]
high = ["tret", "tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]


def change(s):
    if s.isdigit():
        s, i = divmod(int(s), 13)
        if i == 0 and s < 13:
            return high[s]
        else:
            res = low[i]
            while s > 0:
                s, i = divmod(s, 13)
                res = high[i] + " " + res
            return res
    else:
        l = s.split()
        if len(l) == 1:
            if l[0] in low:
                return low.index(l[0])
            else:
                return 13 * high.index(l[0])
        else:
            res = low.index(l.pop())
            l.reverse()
            for i in range(len(l)):
                res += 13 ** (i + 1) * high.index(l[i])
            return res


n = int(input())
for _ in range(n):
    s = input()
    res = change(s)
    print(res)
