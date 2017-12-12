def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b


while True:
    number = input("어서옵쇼. 두 수를 입력하세요 (종료를 원하시면 1을 입력해 주세요): ")

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

            print(sub(int(one), int(two)))
            print(mul(int(one), int(two)))
            print(div(int(one), int(two)))

        except:
            pass

        try:
            int(one) / int(two)
        except ZeroDivisionError:
            print("이 녀석아! 두 번째 입력에서 0을 입력했다네. 분모는 0이 되어서는 안 돼!!!")

        try:
            int(one) and two
        except:
            print("죄송합니다. 첫 번째 입력이 %s입니다. 숫자를 입력하세요" % one)

        try:
            one and int(two)
        except:
            print("죄송합니다. 두 번째 입력이 %s입니다. 숫자를 입력하세요" % two)

