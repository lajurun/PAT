s = input()
p, pa, pat = 0, 0, 0
for i in s:
    if i == "P":
        p += 1
    elif i == "A":
        pa += p
    else:
        pat += pa

print(pat % 1000000007)
