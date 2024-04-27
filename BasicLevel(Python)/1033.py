bad_char = tuple(map(lambda x: x.lower() if x.isupper else x, input()))
all_char = list(input())
output_char = []

for i in all_char:
    if i in bad_char:
        continue
    elif "+" in bad_char and i.isupper():
        continue
    elif i.isalpha() and i.lower() in bad_char:
        continue
    output_char.append(i)

print("".join(output_char))
