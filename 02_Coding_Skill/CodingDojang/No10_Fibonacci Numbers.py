# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
# 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?


def Fibonacci_Numbers():
    number = int(input("피보나치 수열 중, 짝수이면서 N 이하의 모든 항을 더할 범위 N을 입력하시오: "))
    start_number = [1, 2]
    sum_number = 0

    for i in range(1, number):
        if start_number[i] <= number:
                start_number.append((start_number[i-1]+start_number[i]))
        else:
            break

    for j in start_number:
        if j <= number and j % 2 == 0:  # 짝수 -> n % 2 == 0
            sum_number += j
        else:
            continue

    print(sum_number)

while True:
    Fibonacci_Numbers()