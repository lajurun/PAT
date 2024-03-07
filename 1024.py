top, p, tail = input().partition("E")

tail = int(tail)
res = "" if float(top) >= 0 else "-"
t, _, w = top.partition(".")

if tail < 0:
    res = res + "0." + ("0" * (abs(tail)-1)) + str(int(t)) + w
elif abs(tail) == 0:
    res = res + str(abs(int(t))) + "." + w
elif 0 < tail < len(w):
    res = res + str(abs(int(t))) + w[:abs(tail)] + "." + w[abs(tail):]
else:
    res = res + str(abs(int(t))) + w + ("0" * (abs(tail)-len(w)))

print(res)
