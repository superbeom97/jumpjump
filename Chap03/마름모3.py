star = '*'
blank = " "
horizontal_line = '-'
vertical_line = '|'
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
    else: # 사각형 윗부분
        horizontal_line_count = int(number*1)
        blank_count = 1
        print(blank*blank_count, end="")
        print(horizontal_line*horizontal_line_count, end="")
        print(blank*blank_count)

    if number == 1: # 별 하나일 때 양쪽에 수직선 하나씩 추가한 명령문
        vertical_line_count = 1
        horizontal_line_count = int(number*1)
        print(vertical_line*vertical_line_count, end="")
        print(star, end="")
        print(vertical_line*vertical_line_count)
        print(blank*blank_count, end="")
        print(horizontal_line*horizontal_line_count, end="")
        print(blank*blank_count)
        continue
    else:  # 별 2개 이상일 때, 윗삼각형 모양 양쪽에 수직선 하나씩 추가한 명령문
        star_count = 1
        blank_count = int((number - star_count)/2)
        vertical_line_count = 1
        while True:
            print(vertical_line*vertical_line_count, end="")
            print(blank*blank_count, end="")
            print(star*star_count, end="")
            print(blank*blank_count, end="")
            print(vertical_line*vertical_line_count)
            if number == star_count:
                break
            star_count += 2
            blank_count -= 1

    while True: # 역삼각형 모양 양쪽에 수직선 하나씩 추가한 명령문
            star_count -= 2
            blank_count += 1
            vertical_line_count = 1
            print(vertical_line*vertical_line_count, end="")
            print(blank * blank_count, end="")
            print(star * star_count, end="")
            print(blank * blank_count, end="")
            print(vertical_line*vertical_line_count)
            if star_count == 1:
                break

    while True: # 사각형 밑부분
            if number != 1:
                horizontal_line_count = int(number * 1)
                blank_count = 1
                print(blank * blank_count, end="")
                print(horizontal_line * horizontal_line_count, end="")
                print(blank * blank_count)
                break