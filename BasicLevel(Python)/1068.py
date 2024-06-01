def judge(l, i, j, tol):
    around = []
    for x in ([-1, 0, 1]):
        for y in ([-1, 0, 1]):
            if x == 0 and y == 0:
                continue
            tmp = 0
            try:
                tmp = l[i+x][j+y]
            except:
                tmp = 0
            around.append(tmp)
    for t in around:
        if abs(l[i][j] - t) <= tol:
            return False
    else:
        return True


def handle(l, m, n, tol):
    if m == n == 1:
        if l[0][0] > tol:
            print("(1, 1): {}".format(l[0][0]))
        else:
            print("Not Exist")
        return
    else:
        count = 0
        res = []
        for i in range(0, n):
            for j in range(0, m):
                if d[l[i][j]] != 1:
                    continue
                else:
                    if judge(l, i, j, tol):
                            count += 1
                            res = [i, j, l[i][j]]
                            if count > 1:
                                print("Not Unique")
                                return
        if res:
            print("({}, {}): {}".format(res[1]+1, res[0]+1, res[2]))
        else:
            print("Not Exist")
        return


m, n, tol = map(int, input().split())
l = []
d = {}
for _ in range(n):
    sub = [int(x) for x in input().split()]
    l.append(sub)
    for i in sub:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1


handle(l, m, n, tol)
