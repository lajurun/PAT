p, a = input().split()
gp, sp, kp = map(int, p.split("."))
ga, sa, ka = map(int, a.split("."))

p = (gp * 17 + sp) * 29 + kp
a = (ga * 17 + sa) * 29 + ka
n = a - p
sign = "" if n >= 0 else "-"
s, k = divmod(abs(n), 29)
g, s = divmod(s, 17)

print("{}{}.{}.{}".format(sign, g, s, k))
