n = int(input())

j_win, y_win = 0, 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    h = a + c
    if b == h and d != h:
        j_win += 1
    if b != h and d == h:
        y_win += 1

print(y_win, j_win)
