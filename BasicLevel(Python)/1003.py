n = int(input())

for i in range(n):
    s = input()
    p_num = s.count("P")
    a_num = s.count("A")
    t_num = s.count("T")
    if p_num != 1 or t_num != 1 or a_num < 1 or p_num+a_num+t_num != len(s):
        print("NO")
        continue

    p_index = s.find("P")
    t_index = s.find("T")
    a_start_num = p_index
    a_mid_num = t_index - p_index - 1
    a_end_num = len(s) - t_index - 1
    if a_end_num == a_start_num * a_mid_num and a_mid_num > 0:
        print("YES")
    else:
        print("NO")
