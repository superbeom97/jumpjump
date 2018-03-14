while True:
    age=int(input("나이를 입력하세요:"))
    if age <= 3:
        print("요금은 무료입니다.")
    elif age >=4 and age <=13:
        print("요금은 2000원입니다.")
    elif age >=14 and age <=18:
        print("요금은 3000원입니다.")
    elif age >=19 and age <=65:
        print("요금은 5000원입니다.")
    else:
        print("요금은 무료입니다.")