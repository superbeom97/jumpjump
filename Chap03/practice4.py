while True:
    age=int(input("나이를 입력하세요:"))
    if age <= 3:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('유아','무료'))
        print("감사합니다. 티켓을 발행합니다.")
    elif age >=4 and age <=13:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('어린이','2000원'))
        select = int(input("1: 현금, 2: 공원전용 신용카드:"))
        if select==2:
            print("%s원 결제되었습니다. 티켓을 발행합니다." %(2000*0.9))
        else:
         charge = int(input("요금을 입력하세요:"))
         if charge <=1999:
            print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." %(2000-charge,charge))
         elif charge ==2000:
            print("감사합니다. 티켓을 발행합니다.")
         else:
            print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." %(charge-2000))
    elif age >=14 and age <=18:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('청소년','3000원'))
        select = int(input("1: 현금, 2: 공원전용 신용카드:"))
        if select==2:
            print("%s원 결제되었습니다. 티켓을 발행합니다." %(3000*0.9))
        else:
         charge = int(input("요금을 입력하세요:"))
         if charge <=2999:
            print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." %(3000-charge,charge))
         elif charge ==3000:
            print("감사합니다. 티켓을 발행합니다.")
         else:
            print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." %(charge-3000))
    elif age >=19 and age <=59:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('성인','5000원'))
        select = int(input("1: 현금, 2: 공원전용 신용카드:"))
        if select==2:
            print("%s원 결제되었습니다. 티켓을 발행합니다." %(5000*0.9))
        else:
         charge = int(input("요금을 입력하세요:"))
         if charge <4999:
            print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." %(5000-charge,charge))
         elif charge ==5000:
            print("감사합니다. 티켓을 발행합니다.")
         else:
            print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." %(charge-5000))
    elif age >=60 and age <=65:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('성인','5000원'))
        select = int(input("1. 현금, 2: 공원전용 신용카드:"))
        if select==2:
            print("%s원 결제되었습니다. 티켓을 발행합니다." %(5000*0.85))
        else:
            charge = int(input("요금을 입력하세요:"))
            if charge < 4999:
                print("%s원이 모자랍니다. 입력하신 %s원을 반환합니다." % (5000 - charge, charge))
            elif charge == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (charge - 5000))
    else:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('노인','무료'))
        print("감사합니다. 티켓을 발행합니다.")