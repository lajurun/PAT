secret, m = input().split()
m = int(m)

count = 0
while True:
    s = input()
    count += 1
    if count > m:
        print("Account locked")
        break
    if s == "#":
        break
    else:
        if s == secret:
            print("Welcome in")
            break
        else:
            print("Wrong password: {}".format(s))
