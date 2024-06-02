def judge(n1, n2, b):
    if n1 > n2 and b == 0:
        return True
    elif n1 < n2 and b == 1:
        return True
    else:
        return False


own, k = map(int, input().split())

for _ in range(k):
    n1, b, t, n2 = map(int, input().split())

    if own < t:
        print("Not enough tokens.  Total = {}.".format(own))
        continue
    else:
        if judge(n1, n2, b):
            own += t
            print("Win {}!  Total = {}.".format(t, own))
        else:
            own -= t
            if own <= 0:
                print("Lose {}.  Total = {}.".format(t, 0))
                print("Game Over.")
                break
            else:
                print("Lose {}.  Total = {}.".format(t, own))
