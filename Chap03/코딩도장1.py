three = 0
three_sum = 0
five = 0
five_sum = 0
fifteen = 0
fifteen_sum = 0
while True:
    three_mul = three + 3 # 3
    five_mul = five + 5 # 5
    fifteen_mul = fifteen +15 # 15
    if 0 <= three < 1000:
        while True:
            three_sum = three_sum + three_mul # 3+6+9
            three_mul += 3 # 6 9
            if three_mul >= 1000:
                break

    if 0 <= five < 1000:
        while True:
            five_sum = five_sum + five_mul
            five_mul += 5
            if five_mul >= 1000:
                break

    if 0 <= fifteen < 1000:
        while True:
            fifteen_sum = fifteen_sum + fifteen_mul
            fifteen_mul += 15
            if fifteen_mul >= 1000:
                break

    total = three_sum + five_sum - fifteen_sum
    print(total)
    break