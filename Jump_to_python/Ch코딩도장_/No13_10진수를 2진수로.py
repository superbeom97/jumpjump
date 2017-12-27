# 2진법으로 자연수 나타내기
#
# 2진법이란, 어떤 자연수를 0과 1로만 나타내는 것이다.
# 예를 들어 73은 64(2^6)+8(2^3)+1(2^0)이기 때문에 1001001으로 표현한다.
# 어떤 숫자를 입력받았을 때 그 숫자를 2진법으로 출력하는 프로그램을 작성하시오.


## Ver.1 bin 함수를 써서 간략하게 나타낸 버전
def Binary_Number():
    number = int(input("2진법으로 나타내고 싶은 자연수를 입력하시오: "))
    print(bin(number)[2:])

while True:
    Binary_Number()


## Ver.2 bin 함수를 사용하지 않고 10진수를 2진수로 바꾼 버전
def Binary_Number():
    number = int(input("2진법으로 나타내고 싶은 자연수를 입력하시오: ")) # 몫
    rest = []  # 나머지
    binary_number = ""

    while True:
        if number != 0:
            rest.append(number % 2) # 2진수로 나타낸 것이 거꾸로 정렬되어 있어
            number = number // 2

        else:
            for i in range(1, len(rest) + 1):
                binary_number += str(rest[-i]) # 거꾸로 정렬된 것을 뒤집기 위해, 끝에 있는 것을 앞으로

            print(binary_number)
            break

while True:
    Binary_Number()