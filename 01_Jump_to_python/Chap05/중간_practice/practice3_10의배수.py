def ten(number):
    if number % 10 == 0:
        return True
    else:
        return False

while True:
    number = int(input("양수를 입력하세요 (종료를 원하시면 -1을 입력해 주세요): "))

    if number == -1:
        print("이용해 주셔서 감사합니다.")
        break

    elif number == 0 or number <= -2:
        print("양수만 입력해 주세요:)")
        continue

    else:
        print(ten(number))