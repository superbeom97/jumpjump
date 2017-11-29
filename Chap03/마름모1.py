star='*'
blank= ""
while True:
    print("<<마름모 프로그램 연습 ver1.0>>")
    number = int(input("홀수를 입력하세요(프로그램 종료=0):"))
    if number >= 1 and number % 2 != 0:
        for i in range(number+1):
            if i % 2 != 0:
                print(i*star)
    elif number % 2 ==0 and number != 0:
        print("짝수를 입력하셨습니다. 다시 입력하세요")
        continue
    else:
        if number == 0:
            print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
            break