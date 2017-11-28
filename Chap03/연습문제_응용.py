#마름모 출력
#사용자 입력(홀수) , 짝수를 입력 받으면 -> 홀수를 입력하세요, 0 -> 프로그램 종료
#*       *         *
#       ***       ***
#        *       *****
#                 ***
#                  *

while True:
    number = int(input("홀수를 입력하세요(프로그램 종료:0):"))
    if not number==0:
        if number>=1 and number%2!=0:
            print("%s %s %s" %(''*(number-2),'*',''*(number-2)))
            print("%s" %'*'*number)
        else: continue
    else:
        if number==0:
            print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
            break


# i, i