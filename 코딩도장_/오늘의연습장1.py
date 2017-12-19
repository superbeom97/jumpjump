total_num = 0
for i in range(10, 21):
    sum_num = 1
    for j in range(len(str(i))):
        sum_num = sum_num * int(str(i)[j])
    total_num += sum_num

print(total_num)

# 10 11 12 13 14 15 16 17 18 19 20
# 0 1 2 3 4 5 6 7 8 9 0