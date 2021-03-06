# 3n+1 Problem
#
# 어떤 정수 n에서 시작해, n이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다.
# 이렇게 해서 새로 만들어진 숫자를 n으로 놓고, n=1 이 될때까지 같은 작업을 계속 반복한다.
# 예를 들어, n=22이면 다음과 같은 수열이 만들어진다.
#
# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#
# n이라는 값이 입력되었을때 1이 나올때까지 만들어진 수의 개수(1을 포함)를 n의 사이클 길이라고 한다.
# 위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다.
#
# i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수(i, j포함)에 대해 최대 사이클 길이를 구하라.
#
# <<입력 예>>
# 1    10
# 100  200
# 201  210
# 900  1000
#
# <<출력 예>>
# 1    10    20
# 100  200   125
# 201  210   89
# 900  1000  174


def Three_One():
    range_number = input("최대 사이클 길이를 알아보고 싶은 범위를 입력하시오: ")
    range_number_sort = range_number.split()
    first_number = range_number_sort[0]
    second_number = range_number_sort[1]

    initial_number = 0
    for i in range(int(first_number), int(second_number)+1):
        add_number = []
        add_number.append(i)
        while True:
            if i != 1:
                if i % 2 == 0:
                    i = i / 2
                    add_number.append(int(i))
                    continue
                else:
                    i = (i * 3) + 1
                    add_number.append(int(i))
                    continue
            else:
                if len(add_number) > initial_number:
                    initial_number = len(add_number)
                    break
                else:
                    break

    print("%s, %s 사이의 최대 사이클 길이는 '%s'입니다." % (first_number, second_number, initial_number))

while True:
    Three_One()