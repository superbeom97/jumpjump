number = input("숫자를 입력하세요:")
print(number)
if number > 0:
    print("양수")  # 이렇게 하면 안 돼. 제일 위에꺼는 문자열이고 밑에껀 숫자형이므로


number = int(input("숫자를 입력하세요:")) # 위의 문자열을 숫자형으로 바꿔 줘야 돼 int를 붙여서
print(number)
if number > 0:
    print("양수")