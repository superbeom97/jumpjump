grade={'유아':'무료','어린이':'2000원','청소년':'3000원','성인':'5000원','노인':'무료'}
while True:
    age=int(input("나이를 입력하세요:"))
    if age <=3:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('유아',grade.get('유아')))
    elif age >=4 and age <=13:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('어린이',grade.get('어린이')))
    elif age >=14 and age <=18:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('청소년',grade.get('청소년')))
    elif age >=19 and age <=65:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('성인',grade.get('성인')))
    else:
        print("귀하는 %s등급이며, 요금은 %s입니다." %('노인',grade.get('노인')))