people=0
annualticket=5
freeticket=3
guest={'유아':0,'어린이':2000,'청소년':3000,'성인':5000}
grade=""  # 딕셔너리에서 key 값을 통해 value 를 꺼내기 위해_1
while True:
    age=int(input("나이를 입력하세요:"))
    if age <= 3 and age >=1:
         print("귀하는 %s등급이며, 요금은 %s원입니다." %('유아',0))
         print("감사합니다. 티켓을 발행합니다.")
    elif age >=4 and age <=13:
         print("귀하는 %s등급이며, 요금은 %s원입니다." % ('어린이', 2000))
         grade = "어린이" # 딕셔너리에서 key 값을 통해 value 를 꺼내기 위해_2
    elif age >=14 and age <=18:
         print("귀하는 %s등급이며, 요금은 %s원입니다." % ('청소년', 3000))
         grade = "청소년" # 딕셔너리에서 key 값을 통해 value 를 꺼내기 위해_3
    elif age >=19 and age <=65:
         print("귀하는 %s등급이며, 요금은 %s원입니다." % ('성인', 5000))
         grade = "성인" # 딕셔너리에서 key 값을 통해 value 를 꺼내기 위해__4
    elif age >= 66:
          print("귀하는 %s등급이며, 요금은 %s원입니다." % ('노인', 0))
          print("감사합니다. 티켓을 발행합니다.")
    else:
        print("나이를 올바르게 입력해주세요")
        continue

    if age >= 4 and age <= 65:
        select = int(input("1: 현금, 2: 공원전용 신용카드:"))
        if select == 1:
            charge = int(input("요금을 입력하세요:"))
            if charge < guest[grade]:
                print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." % ((guest[grade]-charge), charge))
            elif charge == guest[grade]:
                print("감사합니다. 티켓을 발행합니다.")
                people+=1
            elif charge > guest[grade]:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (charge-guest[grade]))
                people+=1
        elif select == 2:
            people+=1
            if age >= 4 and age <= 59:
                print("%s원 결제되었습니다. 티켓을 발행합니다." % int(guest[grade]*0.9))
            else:
                print("%s원 결제되었습니다. 티켓을 발행합니다." % int(guest[grade]*0.9*0.95))
        else:
            print("1 또는 2를 입력하세요")
            continue

    if people % 7 == 0 and people != 0:
        if freeticket <= 0: continue
        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %s장" % (freeticket-1))
        freeticket -= 1
    elif people % 4 ==0 and people != 0:
        if annualticket <= 0 :continue
        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %s장" % (annualticket-1))
        annualticket -= 1