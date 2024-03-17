# 题目有点没有读懂

n = int(input())

for i in range(n):
    s = input()
    p = s.count("P")
    a = s.count("A")
    t = s.count("T")
    if p != 1 or t != 1 or a < 1 or p+a+t != len(s):
        print("NO")
        continue

    a_p = s.find("P")
    a_t = s.find("T")
    p_t = a_t - a_p - 1
    t_a = len(s) - a_t - 1
    if t_a == a_p * p_t and p_t > 0:
        print("YES")
    else:
        print("NO")