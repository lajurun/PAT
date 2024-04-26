n = int(input())

data_dict = {}

max_s, max_p = map(int, input().split())
data_dict[max_s] = max_p

for _ in range(n - 1):
    s, p = map(int, input().split())

    if data_dict.get(s):
        data_dict[s] += p
    else:
        data_dict[s] = p

    if data_dict[s] > max_p:
        max_s, max_p = s, data_dict[s]

print(max_s, max_p)
