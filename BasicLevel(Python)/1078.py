def compress(s):
    length = len(s)
    res = ""
    count = 1
    for i in range(length-1):
        if s[i+1] == s[i]:
            count += 1
        else:
            if count == 1:
                res += s[i]
            else:
                res += str(count) + s[i]
            count = 1
    if count == 1:
        res += s[-1]
    else:
        res += str(count) + s[-1]
    print(res)


def decompress(s):
    length = len(s)
    res = ""
    count = ""
    for i in s:
        if i.isdigit():
            count += i
        else:
            if count:
                res += int(count) * i
                count = ""
            else:
                res += i
    print(res)


tag = input()
s = input()
if tag == "C":
    compress(s)
else:
    decompress(s)
