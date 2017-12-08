while True:
    age = int(input("나이를 입력해 주세요:)\n종료를 원하시면 0을 입력해 주세요 :"))

    if age < 0:
        print("나이를 올바르게 입력해 주세요")
        continue

    elif age == 0:
        print("이용해 주셔서 감사합니다.")
        break

    else:
        if 1 <= age <= 2:
            print("반갑습니다. 무료로 입장하시면 됩니다!")
        elif 3 <= age <= 12:
            print("반갑습니다. 입장료를 10달러입니다.")
        else:
            print("반갑습니다. 입장료는 15달러입니다.")