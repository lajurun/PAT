def judge(s):
    length = len(s)
    if length == 1:
        return True

    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


s = input()

if judge(s):
    print("{} is a palindromic number.".format(s))
else:
    for _ in range(10):
        tmp = "".join(reversed(s))
        sums = str(int(s) + int(tmp))
        print("{} + {} = {}".format(s, tmp, sums))
        s = sums
        if judge(s):
            print("{} is a palindromic number.".format(s))
            break
    else:
        print("Not found in 10 iterations.")
