# Primary Arithmetic
#
# <<첫 번째 계산>>
# 아이들은 여러 자리 숫자들을 더하기 위해서 우에서 좌로 숫자를 하나씩 차례대로 더 하라고 배웠다.
# 1을 한 숫자 위치에서 다음 자리로 더하기위해 이동하는
# "한자리올림"연산을 많이 발견하는 것은 중요한 도전이 된다.
# 당신의 일은 교육자가 그들의 어려움을 평가하기 위하여
#
# 덧셈 문제들의 각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.
#
# <<입력>>
# 입력의 각 라인은 10개의 숫자들보다 미만인 양의 정수들 두 개를 포함한다.
# 입력의 마지막 라인은 0 0 을 포한한다.
#
# <<출력>>
# 마지막을 제외한 입력의 각 라인에 대해서
# 당신은 두 숫자들을 더한 결과에서 한자리올림 연산들의 수를 아래 처럼 보여지는 형식으로 계산하여 출력해야 한다.
#
# <<입력 샘플>>
# 123 456
# 555 555
# 123 594
# 0 0
#
# <<출력 샘플>>
# No carry operation.
# 3 carry operations.
# 1 carry operation.

def Primary_Arithmetic():
    count = 0
    total_count = []    # [0, 0, 2, 3, 1]
    first_number = ""
    second_number = ""
    print("두 수를 더해 한 자리 올림의 개수를 찾아주는 프로그램입니다.")
    print("더하고자 하는 두 수를 입력해 주세요.")
    print("입력을 다 하셨으면 '0 0'을 입력해 주세요.")

    while True:
        total_count.append(count)
        count = 0
        want_arithmetic = input()
        if want_arithmetic != "0 0":
            sort_arithmetic = want_arithmetic.split()
            first_number = sort_arithmetic[0]
            second_number = sort_arithmetic[1]
            if len(first_number) >= len(second_number):
                plus_count = 0
                for i in range(len(second_number)):
                    if int(first_number[-(i + 1)]) + int(second_number[-(i + 1)]) + plus_count >= 10:
                        plus_count = 0
                        count += 1
                        plus_count += 1
                    else:
                        continue
            else:
                plus_count = 0
                for i in range(len(first_number)):
                    if int(first_number[-(i + 1)]) + int(second_number[-(i + 1)]) + plus_count >= 10:
                        plus_count = 0
                        count += 1
                        plus_count += 1
                    else:
                        continue
        else:
            for j in total_count[1:]:
                if j == 0:
                    print("No carry operation.")
                elif j == 1:
                    print("1 carry operation.")
                else:
                    print("%s carry operations." % j)


Primary_Arithmetic()