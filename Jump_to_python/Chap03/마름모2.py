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
        star_count -= 2
        blank_count += 1
        print(blank * blank_count, end="")
        print(star * star_count)
        if star_count == 1:
            break