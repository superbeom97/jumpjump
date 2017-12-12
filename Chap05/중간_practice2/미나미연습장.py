def sum(a, b):
    return a + b

while True:
    try:
        number = input("어서옵쇼. 두 수를 입력하세요 (종료를 원하시면 1을 입력해 주세요): ")
        berry = number.split()
        # one = int(berry[0])
        # two = int(berry[1])

        if berry[0] and berry[1]:
            print(sum(int(berry[0]), int(berry[1])))
            continue

        elif int(berry[0]) == 1 and berry[1] == " ":
            print("이용해 주셔서 감사합니다.")
            break

    except:
        if int(berry[0]) and berry[1]:
            print("죄송합니다. 두 번째 입력이 %s입니다. 숫자를 입력하세요." % berry[1])
            continue
    #
    #     elif one_str and two:
    #         print("죄송합니다. 첫 번째 입력이 %s입니다. 숫자를 입력하세요." % one_str)
    #         continue
    #
    #     elif one_str and two_str:
    #         print("죄송합니다. 첫 번째 입력이 %s이고 두 번째 입력이 %s입니다. 숫자를 입력하세요." % (one_str, two_str))
    #         continue