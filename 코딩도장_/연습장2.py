def Fibonacci_Numbers(number):
    start_number = [1, 2]
    sum_number = 0

    for i in range(1, number+1):
        try:
            continue
        except:
            if start_number[i+1] <= 400:
                start_number.append((start_number[i] + start_number[i+1]))
            else:
                continue

        for j in start_number:
            if j <= 400 and j % 2 == 0:
                sum_number += j
            else:
                continue

        print(sum_number)

Fibonacci_Numbers(10)