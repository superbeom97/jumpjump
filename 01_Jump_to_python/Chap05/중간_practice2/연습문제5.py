def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b


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
            int(one) and int(two)
            print(sum(int(one), int(two)))
            print(sub(int(one), int(two)))
            print(mul(int(one), int(two)))
            print(div(int(one), int(two)))

        except ZeroDivisionError: # div 때문에 두 개로 나눠서 해봤었다. (sum/sub/mul vs div) 하지만 int(one) and int(two) 똑같았고.. 함께 묶는 방법을 생각하면서
            print("이 녀석아! 두 번째 입력에서 0을 입력했다네. 분모는 0이 되어서는 안 돼!!!") # except만 나누는 방법을 생각함.
            continue

        except:
            pass

        try:
            int(one) and two # 실제 입력은 one 문자 two 숫자 // one 숫자 two 문자
        except:
            print("죄송합니다. 첫 번째 입력이 %s입니다. 숫자를 입력하세요." % one)

        try:
            one and int(two) # 실제 입력 one 숫자 two 0
        except:
            print("죄송합니다. 두 번째 입력이 %s입니다. 숫자를 입력하세요." % two)
            continue