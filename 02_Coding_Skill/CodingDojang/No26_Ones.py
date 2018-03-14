# Ones
#
# 2나 5로 나눌 수 없는 0 이상 10,000 이하의 정수 n이 주어졌는데,               ## n % 2 != 0 and n % 5 != 0
# n의 배수 중에는 10진수로 표기했을 때 모든 자리 숫자가 1인 것이 있다.
#
# 그러한 n의 배수 중에서 가장 작은 것은 몇 자리 수일까?
#
# <<Sample Input>>
# 3
# 7
# 9901
#
# <<Sample Output>>
# 3
# 6
# 12


def Ones():
    number_n = int(input("2와 5로 나눌 수 없는 정수 하나를 입력하시오: "))
    if number_n % 2 != 0 and number_n % 5 !=0:
        number_n_group = "2" # 123
        one_check_group = ""
        check_group = ""

        if number_n == 1 or number_n == 11 or number_n == 111 or number_n == 1111:
            print(len(number_n))

        else:
            count = 2
            while True:
                check_group = ""
                for j in number_n_group:
                    if int(j) == 1:
                        check_group += j
                    else:
                        continue

                if number_n_group == check_group:
                    print(len(number_n_group))
                    break
                else:
                    number_n_group = ""
                    number_n_group = str(number_n * count)
                    count += 1

    else:
        print("2와 5로 나눌 수 있는 정수를 입력했잖니!!!!")

while True:
    Ones()