three_range = range(1000)
five_range = range(1000)
fifteen_range = range(1000)
three_sum = 0
five_sum = 0
fifteen_sum = 0
for three in three_range:
    if three % 3 != 0:
        three_sum = three_sum + three
    else:
        break

for five in five_range:
    if five % 5 != 0:
        five_sum = five_sum + five
    else:
        break

for fifteen in fifteen_range:
    if fifteen % 15 != 0:
        fifteen_sum = fifteen_sum + fifteen
    else:
        break

total = three_sum + five_sum - fifteen_sum
print(total)