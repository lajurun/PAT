s = input()
s_dict = {}
tag = True
for i in s:
    if i.isalpha():
        i = i.lower()
        if tag:
            max_s, max_count = i, 1
            tag = False

        if s_dict.get(i):
            s_dict[i] += 1
            if s_dict[i] > max_count:
                max_s, max_count = i, s_dict[i]
            elif s_dict[i] == max_count:
                if i < max_s:
                    max_s, max_count = i, s_dict[i]
            else:
                pass
        else:
            s_dict[i] = 1

    else:
        continue

print(max_s, max_count)
