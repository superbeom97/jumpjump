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
        if j <= number and j % 2 == 0:
            sum_number += j
        else:
            continue

    print(sum_number)

while True:
    Fibonacci_Numbers()