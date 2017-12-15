def GuGu(number):
    print("<%s단>" % int(number))
    i = 0
    while True:
        if i == 9:
            break
        for i in range(1, 10):
            result = "%s * %s = %s" % (int(number), i, (i * int(number)))
            print(result)


while True:
    number = input("숫자를 입력하세요(종료 : -1 // 구구단 전체 출력 : all) : ")

    if number == "all":
        for j in range(2, 10):
            GuGu(j)

    elif 2 <= int(number) <= 9:
        GuGu(number)

    elif int(number) == -1:
        print("이용해 주셔서 감사합니다.")
        break

    else:
        try:
            raise int(number) < -1

        except:
            print("ValueError exception")