n = int(input())

for _ in range(n):
    s = input().strip()
    if len(s) < 6:
        print("Your password is tai duan le.")
        continue
    tag1 = False
    tag2 = False
    for i in s:
        if i.isalpha() or i.isdigit() or i == ".":
            if i.isalpha():
                tag1 = True
            if i.isdigit():
                tag2 = True
        else:
            print("Your password is tai luan le.")
            break
    else:
        if tag1 and tag2:
            print("Your password is wan mei.")
        if tag1 and not tag2:
            print("Your password needs shu zi.")
        if not tag1 and tag2:
            print("Your password needs zi mu.")
