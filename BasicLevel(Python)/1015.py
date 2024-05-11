# 源代码地址：https://blog.csdn.net/letv0907/article/details/104788854
# 第一个优化点：input() 改成 sys.stdin.readline()，print() 改成 sys.stdout.write()
# 第二个优化点：将德分和才分转int，改成从字典里面取值
# 第三个优化点：优化存储结构
# 第四个优化点：把代码放到定义的函数里面执行
# 这里只用到了前面2个优化点，就可以全部通过了

import sys


n, l, h = map(int, sys.stdin.readline().split())
l1, l2, l3, l4 = [], [], [], []
score_dict = dict(zip([str(i) for i in range(101)], range(101)))

for j in range(n):
    k, d, c = sys.stdin.readline().split()
    d, c = score_dict[d], score_dict[c]

    if d < l or c < l:
        continue
    elif d >= h and c >= h:
        l1.append((k, d, c))
    elif d >= h and c < h:
        l2.append((k, d, c))
    elif d >= c:
        l3.append((k, d, c))
    else:
        l4.append((k, d, c))


def st(lst):
    return -(lst[1] + lst[2]), -lst[1], lst[0]


print(len(l1) + len(l2) + len(l3) + len(l4))

for i in (l1, l2, l3, l4):
    i.sort(key=st)
    for j in i:
        j = " ".join([str(a) for a in j])
        sys.stdout.write(j + "\n")
