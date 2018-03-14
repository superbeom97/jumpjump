while True:
    print("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.")
    number = int(input("1. 주문\n2. 종료\n입력 : "))

    if number <= 0 or number >= 3:
        print("올바른 숫자를 입력해 주세요.")
        continue

    elif number == 1:
        make_sandwiches_list = []

        while True:
            input_ingredient = str(input("안녕하세요. 원하시는 재료를 입력하세요: "))

            if input_ingredient != '종료':
                make_sandwiches_list.append(input_ingredient)
                continue

            elif input_ingredient == '종료':
                print("샌드위치를 만들겠습니다.")

                for i in make_sandwiches_list:
                    print("%s 추가합니다." % i)

                print("여기 주문하신 샌드위치를 만들었습니다. 맛있게 드세요:)")
                break

    elif number == 2:
        print("감사합니다. 다음에 또 방문해 주세요:)")
        break