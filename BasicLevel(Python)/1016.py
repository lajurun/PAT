a, d_a, b, d_b = input().split()

p_a = d_a * a.count(d_a) if a.count(d_a) else '0'
p_b = d_b * b.count(d_b) if b.count(d_b) else '0'

print(int(p_a) + int(p_b))
