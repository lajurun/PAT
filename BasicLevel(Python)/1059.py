def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


n = int(input())
all_id = {"ni": "hao"}
for i in range(n):
    all_id[input()] = i + 1

checked_id = set()
k = int(input())
for _ in range(k):
    tmp = input()
    if tmp not in all_id:
        print("{}: Are you kidding?".format(tmp))
    elif tmp in checked_id:
        print("{}: Checked".format(tmp))
    elif all_id[tmp] == 1:
        print("{}: Mystery Award".format(tmp))
    elif is_prime(all_id[tmp]):
        print("{}: Minion".format(tmp))
    else:
        print("{}: Chocolate".format(tmp))
    checked_id.add(tmp)
