# 此题python解不了，测试能过，提交全部非零返回
# 大佬测试：https://blog.csdn.net/q839219286/article/details/93635134


def handle_string(s):
    l = []
    tag = False
    res = ""
    for i in s:
        if tag:
            if i == "]":
                l.append(res)
                tag = False
                res = ""
            else:
                res += i
        if i == "[" and not tag:
            tag = True
            continue
    return l


hands = handle_string(input())
eyes = handle_string(input())
mouth = handle_string(input())
length_hands = len(hands)
length_eyes = len(eyes)
length_mouth = len(mouth)

n = int(input())
for _ in range(n):
    l = list(map(lambda x: int(x)-1, input().split()))
    if l[0] >= length_hands or l[4] >= length_hands or l[1] >= length_eyes or l[3] >= length_eyes or l[2] >= length_mouth:
        print("Are you kidding me? @\/@")
    else:
        print("{}({}{}{}){}".format(hands[l[0]], eyes[l[1]], mouth[l[2]], eyes[l[3]], hands[l[4]]))
