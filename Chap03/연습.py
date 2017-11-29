star = '*'
for i in range(1, 10):
    print(i*star, end=' ')
print('')

star = '*'
while True:
    number = int(input("홀수를 입력하세요(프로그램 종료 = 0):"))
    if number >= 1 and number % 2 != 0:
        print(star*number)
    if i % 2 == 0: continue
    if i > 5: continue
    print("*"*i)

star='*'
blank=" "
#line=
while True:
    customer = int(input("홀수를 입력하세요(프로그램 종료=0):"))
    if customer >= 1 and customer % 2 != 0:
        for i in range(10):
            print(i*star, end=" ")
        print('')
    elif customer % 2 ==0 and customer != 0:
        print("짝수를 입력하셨습니다. 다시 입력하세요")
        continue
    else:
        if customer == 0:
            print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
            break