rates_count = input()
rates_string = input()
rates = rates_string.split(' ')
rates_int = map(int, rates)

counts_dict = dict()
for i in rates_int:
    counts_dict[i] = counts_dict.get(i, 0) + 1

cd = dict(sorted(counts_dict.items()))

total_buy_want = 0
previous_set_last_key = 10000
while len(cd) != 0:
    total_buy_want += (len(cd) - 1)
    if previous_set_last_key < list(cd)[0]:
        total_buy_want += 1

    previous_set_last_key = list(cd)[-1]

    cd = {key: value - 1 for key, value in cd.items() if value != 1}

print('total_buy_want', total_buy_want)
