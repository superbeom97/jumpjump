star = '*'
blank = " "
while True:
    print("<<마름모 프로그램 연습 ver1.0>>")
    number = int(input("홀수를 입력하세요(프로그램 종료=0):"))
    if number == 0:
        print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
        break
    elif number % 2 == 0:
        print("짝수를 입력하셨습니다. 다시 입력하세요")
        continue
    elif number < 0:   # 입력하는 숫자가 0보다 작을 때 계속 별이 그려지는 것을 수정하기 위해 추가
        print("홀수를 다시 입력하세요")
        continue
    elif number == 1: # 1 쳤을 때 별이 계속 그려지는 것을 수정하기 위해 추가
        print(star)  # 1 쳤을 때 별이 계속 그려지는 것을 수정하기 위해 추가
        continue  # 1 쳤을 때 별이 계속 그려지는 것을 수정하기 위해 추가
    else:
        star_count = 1
        blank_count = int((number - star_count)/2)
        while True:
            print(blank*blank_count, end="")
            print(star*star_count)
            if number == star_count:
                break
            star_count += 2
            blank_count -= 1

    while True:
        if number == 1:
            break
        else:
            star_count -= 2
            blank_count += 1
            print(blank * blank_count, end="")
            print(star * star_count)
            if star_count == 1:
                break