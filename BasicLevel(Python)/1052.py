# 源代码地址：https://blog.csdn.net/u012949658/article/details/107474885

import sys


def handle(s):
    l = []
    res = bytes()
    for i in range(len(s) - 1):
        if s[i:i + 1] == b"[":
            res = bytes()
            continue
        if s[i:i + 1] == b"]":
            l.append(res)
            continue
        res += s[i:i + 1]
    return l


hands = handle(sys.stdin.buffer.readline())
eyes = handle(sys.stdin.buffer.readline())
mouth = handle(sys.stdin.buffer.readline())

k = int(input())
for _ in range(k):
    l = []
    try:
        for i in input().split():
            i = int(i) - 1
            if i < 0:
                break
            l.append(i)
        res = hands[l[0]] + b"(" + eyes[l[1]] + mouth[l[2]] + eyes[l[3]] + b")" + hands[l[4]] + b"\n"
        sys.stdout.buffer.write(res)
    except:
        sys.stdout.buffer.write(b"Are you kidding me? @\/@\n")
