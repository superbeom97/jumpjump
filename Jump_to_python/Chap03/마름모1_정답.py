star = '*'
blank = " " # blank = "" 하면 안 됨, 큰따옴표 안에 공백을 넣어 줘야 함
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
        star_count = 1 # 이 변수를 선정하는 게 어렵다,, 처음에 문자 변수 설정 했으면, 그 변수에 대한 또 다른 변수를 생각하자!
        blank_count = int((number - star_count)/2) # 이 변수를 선정하는 게 어렵다,, 처음에 문자 변수 설정 했으면, 그 변수에 대한 또 다른 변수를 생각하자!
        while True:
            print(blank*blank_count, end="")
            print(star*star_count)
            if number == star_count:
                break
            star_count += 2
            blank_count -= 1