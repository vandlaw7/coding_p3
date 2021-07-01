rates_count = input()
rates_string = input()
rates = rates_string.split(' ')
rates_int = map(int, rates)

counts_dict = dict()
for i in rates_int:
    counts_dict[i] = counts_dict.get(i, 0) + 1

counts_dict_sorted = dict(sorted(counts_dict.items()))

cd = counts_dict_sorted.copy()

total_buy_want = 0
previous_set_last_key = 10000
while True:
    buy_want = 0
    first_key = 0
    first_key_bool = True
    for key, value in cd.items():
        if value > 0:
            value -= 1
            buy_want += 1

            if first_key_bool:
                first_key = key
                first_key_bool = False

            last_key = key
        else:
            del cd[key]

    total_buy_want += buy_want - 1
    if previous_set_last_key < first_key:
        total_buy_want += 1

    if all(value == 1 for value in cd.values()):
        total_buy_want += buy_want - 1
        if previous_set_last_key < first_key:
            total_buy_want += 1
        break

print(total_buy_want)




