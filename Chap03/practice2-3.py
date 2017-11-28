age={'유아':'무료','어린이':'2000원','청소년':'3000원','성인':'5000원','노인':'무료'}
while True:
    age=int(input("나이를 입력하세요:"))
    for i in range(len(age)):
        if i==0:
            print("귀하는 %s등급이며, 요금은 %s입니다." %i)
        elif age >=4 and age <=13:
            print("귀하는 %s등급이며, 요금은 %s입니다." %('어린이',age.get('어린이')))
        elif age >=14 and age <=18:
            print("귀하는 %s등급이며, 요금은 %s입니다." %('청소년',age.get('청소년')))
        elif age >=19 and age <=65:
            print("귀하는 %s등급이며, 요금은 %s입니다." %('성인',age.get('성인')))
        else:
            print("귀하는 %s등급이며, 요금은 %s입니다." %('노인',age.get('노인')))