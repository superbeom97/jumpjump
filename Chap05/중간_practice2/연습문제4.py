def sum(a, b):
    return a + b


while True:
    number = input("어서옵쇼. 두 수를 입력하세요 (종료를 원하시면 '종료'를 입력해 주세요): ")

    if number == "종료":
        print("이용해 주셔서 감사합니다.")
        break

    else:
        berry = number.split()
        one = berry[0]
        two = berry[1]

        try:
            one and two
            print(sum(int(one), int(two)))
            # continue # try 자체가 독립적이니 continue 할 필요 없는
        except:
            pass

        try:
            int(one) and two
        except:
            print("죄송합니다. 첫 번째 입력이 %s입니다. 숫자를 입력하세요." % one)

        try:
            one and int(two)
        except:
            print("죄송합니다. 두 번째 입력이 %s입니다. 숫자를 입력하세요." % two)