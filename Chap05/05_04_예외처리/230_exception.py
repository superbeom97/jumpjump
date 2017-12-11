try:
    number = int(input("양수를 입력하세요: "))
    if number < 0 :
        # print("양수를 입력하세요!!")
        raise NegativeNumberinputError

    # f = open("나 없는 파일", 'r')
    # 4/0
    print("Hello World!")

except FileNotFoundError as e:
    print("없는 파일을 열었습니다.")
    print("시스템 에러 메세지: " + str(e))

except ZeroDivisionError:
    print("에러가 발생했습니다.")
    print("0으로 나누었습니다.")

else:
    print("Thank you!!")

finally:
    print("See ya later")

print("프로그램 정상 종료")