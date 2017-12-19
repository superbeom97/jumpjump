def Count_Number():
    number = int(input("1부터 각 숫자의 개수를 구할 범위를 정하시오: "))
    total_num = ""
    for i in range(1, number+1):
        total_num += str(i)

    for j in range(10):
        print("%s의 개수 : %s개" % (j, total_num.count(str(j))))

while True:
    Count_Number()