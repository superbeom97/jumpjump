#마름모 출력
#사용자 입력(홀수) , 짝수를 입력 받으면 -> 홀수를 입력하세요, 0 -> 프로그램 종료
#*       *         *
#       ***       ***
#        *       *****
#                 ***
#                  *


star='*'
blank=" "
while True:
    customer = int(input("홀수를 입력하세요(프로그램 종료:0):"))
    if customer>=1 and customer % 2 !=0:
        blank-=1
        star+=2
        print(blank, end="")
        print(star)
    elif customer % 2 ==0: continue
    else:
        if customer==0:
            print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
            break