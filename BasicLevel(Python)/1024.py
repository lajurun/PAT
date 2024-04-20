top, _, tail = input().partition("E")

tail = int(tail)
t, _, w = top.partition(".")
sign = "" if float(top) >= 0 else "-"

if tail < 0:
    res = sign + "0." + ("0" * (abs(tail)-1)) + str(abs(int(t))) + w
elif tail == 0:
    res = sign + str(abs(int(t))) + "." + w
elif 0 < tail < len(w):
    res = sign + str(abs(int(t))) + w[:abs(tail)] + "." + w[abs(tail):]
else:
    res = sign + str(abs(int(t))) + w + ("0" * (abs(tail)-len(w)))

print(res)
