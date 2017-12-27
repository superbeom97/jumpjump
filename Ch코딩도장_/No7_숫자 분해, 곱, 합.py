# 10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
#
# 예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
#
# 10 = 1 * 0 = 0
#  11 = 1 * 1 = 1
#  12 = 1 * 2 = 2
#  13 = 1 * 3 = 3
#  14 = 1 * 4 = 4
#  15 = 1 * 5 = 5
#
# 그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15


## Ver.1 문제에서 요구한 대로
def Sum_Number(number):
    total_num = 0
    for i in range(10, number+1):
        sum_num = 1
        for j in range(len(str(i))):
            sum_num = sum_num * int(str(i)[j])
        total_num += sum_num

    print(total_num)

Sum_Number(1000)


## Ver.2 범위를 받아서 구하는 버전
def Sum_Number():
    number = int(input("10부터 각 숫자를 분해하여 곱한 것의 전체 합을 구할 범위를 정하시오: "))
    total_num = 0
    for i in range(10, number+1):
        sum_num = 1
        for j in range(len(str(i))):
            sum_num = sum_num * int(str(i)[j])
        total_num += sum_num

    print(total_num)

while True:
    Sum_Number()