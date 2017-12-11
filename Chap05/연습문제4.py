try:
    while True:
        number = str(input("어서옵쇼. 두 수를 입력하세요 (종료를 원하시면 1을 입력해 주세요): "))
        berry = number.split()
        one = int(berry[0])
        one_str = str(berry[0])
        two = int(berry[1])
        two_str = str(berry[1])
        sum = one + two

        if number == 1:
            print("이용해 주셔서 감사합니다.")
            break

        elif one and two:
            print(sum)
            continue

except:
    if one and two_str:
        print("죄송합니다. 두 번째 입력이 %s입니다. 숫자를 입력하세요." % two_str)

    elif one_str and two:
        print("죄송합니다. 첫 번째 입력이 %s입니다. 숫자를 입력하세요." % one_str)

    elif one_str and two_str:
        print("죄송합니다. 첫 번째 입력이 %s이고 두 번째 입력이 %s입니다. 숫자를 입력하세요." % (one_str, two_str))