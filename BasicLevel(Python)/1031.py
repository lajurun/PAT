weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
m = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]


def examine(s):
    sum = 0
    s_list = list(s)

    for i in range(17):
        if s_list[i].isalpha():
            return False
        else:
            sum += int(s_list[i]) * weight[i]

    remainder = sum % 11

    if m[remainder] == s_list[-1]:
        return True
    else:
        return False


n = int(input())
data_input = []
for _ in range(n):
    data_input.append(input())

data_unqualified = []
for data in data_input:
    if not examine(data):
        data_unqualified.append(data)

if data_unqualified:
    for i in data_unqualified:
        print(i)
else:
    print("All passed")
