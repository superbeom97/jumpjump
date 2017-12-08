while True:
    number = str(input("세 개의 양수를 입력하세요\n종료를 원하시면 -1을 입력하세요: "))
    john = "".join(number)
    check = john.split()

    one = int(check[0])

    if one == -1:
        print("이용해 주셔서 감사합니다.")
        break

    else:
        john = "".join(number)
        check = john.split()

        one = int(check[0])
        two = int(check[1])
        three = int(check[2])

        if (one * two) % three == 0:
            print("%s는 %s와 %s의 공배수입니다." % (three, one, two))
            continue

        elif (one * two) % three != 0:
            print("%s는 %s와 %s의 공배수가 아닙니다." % (three, one, two))
            continue