n = int(input())


def to_num(num, h):
    lst = []
    for i in range(4):
        lst.append(num % 10)
        num //= 10

    if h:
        lst.sort(reverse=True)
    else:
        lst.sort()

    return int("".join(map(str, lst)))


while True:
    a = to_num(n, True)
    b = to_num(n, False)
    c = a - b
    print("{:04} - {:04} = {:04}".format(a, b, c))
    n = c
    if c == 6174 or c == 0:
        break
