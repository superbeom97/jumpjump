# 프로그램 실행 순서
# 1.입력할 정수의 개수를 사용자로부터 입력 받는다.
# 2.입력받은 정수의 개수만큼 정수를 입력받는다.
# 3.입력받은 정수의 합과 평균 값을 출력한다.
# 4.할당된 메모리공간을 비운다.
#
# 요구사항
# 1.메모리공간은 사용자의 입력 수의 따라 변동된다.
# 2.사용한 공간은 마지막에 비워야 한다.
# 3.배열(리스트)을 사용하면 안된다.


## Ver.1_배열(리스트)을 사용한 코드
def Number():
    memory = int(input("메모리 공간을 설정하시오: "))
    count_int = int(input("입력할 정수의 개수를 입력하시오: "))
    num_int = input("입력한 정수의 개수만큼 정수를 입력하시오: ")
    num_int_list = num_int.split()

    sum_num = 0
    for i in num_int_list:
        sum_num += int(i)

    avg_num = int(sum_num / count_int)
    memory_num = sum_num + avg_num

    print("입력하신 정수들의 합은 %s입니다." % sum_num)
    print("입력하신 정수들의 평균은 %s입니다." % avg_num)
    print("할당된 메모리 공간 %s을 비웁니다." % memory_num)
    print("남은 메모리 공간은 %s입니다." % (memory - memory_num))

Number()


## Ver.2_배열(리스트)을 사용하지 않은 코드
def Number():
    memory = int(input("메모리 공간을 설정하시오: "))
    count_int = int(input("입력할 정수의 개수를 입력하시오: "))

    print("입력한 정수의 개수만큼 정수를 입력하시오")
    sum_num = 0
    for i in range(count_int):
        num_int = int(input()) # 정수 입력값을 하나씩 받아야 하는!!
        sum_num += num_int

    avg_num = int(sum_num / count_int)
    memory_num = sum_num + avg_num

    print("입력하신 정수들의 합은 %s입니다." % sum_num)
    print("입력하신 정수들의 평균은 %s입니다." % avg_num)
    print("할당된 메모리 공간 %s을 비웁니다." % memory_num)
    print("남은 메모리 공간은 %s입니다." % (memory - memory_num))

Number()