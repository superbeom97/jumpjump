# 100까지의 자연수의 합의 제곱과 제곱의 합의 차이

# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다
# (제곱의 합). 1^2 + 2^2 + ... + 10^2 = 385

# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다
# (합의 제곱). (1 + 2 + ... + 10)^2 = 55^2 = 3025

# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.

# 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?


## Ver.1 처음에 짠 코드
def Sum_Square():
    print("N까지의 자연수의 합의 제곱과 제곱의 합의 차이를 계산하는 프로그램입니다.")
    number = int(input("알아보고 싶은 범위 N을 입력하세요: "))
    sum_number = 0
    square_number = 0

    for i in range(1, number+1):
        sum_number += i

    sum_number = sum_number * sum_number

    for i in range(1, number+1):
        square_number += i * i

    print(sum_number - square_number)

while True:
    Sum_Square()


## Ver.2 중복된 것을 하나로 합친 코드
def Sum_Square():
    print("N까지의 자연수의 합의 제곱과 제곱의 합의 차이를 계산하는 프로그램입니다.")
    number = int(input("알아보고 싶은 범위 N을 입력하세요: "))
    sum_number = 0
    square_number = 0

    for i in range(1, number+1):
        sum_number += i
        square_number += i * i

    sum_number = sum_number * sum_number
    print(sum_number - square_number)

while True:
    Sum_Square()