# 자릿수를 뒤바꿔 곱했을 때 증가수가 되는 수
#
# 어떤 자연수에서 자릿수가 점점 커지는 수를 증가수라고 하겠습니다(예: 135689)
# 자연수들 중에서는 그 수와 그 수의 자리의 순서가 반대인 수를 곱했을 때, 증가수가 되는 수들이 있습니다.
# (여기서 자리의 순서가 반대가 된다는 것은 숫자의 자리가 앞뒤가 바뀐다는 것입니다, 예: 5319 -> 9135)
#
# 예를 들어 47과 47의 자리를 바꾼 74를 곱하면 3478이 되는데, 이 수는 증가수입니다.
#
# 세 자리 자연수들 중에 그 수와 그 수의 자리를 바꾼 수의 곱이 증가수가 되는 수는 모두 몇 개입니까?
#
# (단, 세 자리 자연수의 마지막 자릿수는 0이 아니고,
# 증가수에는 1335 같은 중간에 자릿수의 크기가 바뀌지 않는 것도 포함됩니다.)


# 세 자리 자연수 -> 100 ~ 999
    # 이 중에서 일의 자리가 0인 것 제외하기!
    # 중간에 자릿수의 크기가 바뀌지 않는 것도 제외하는 줄 알았다...어쩐지 코드는 확실한데 안 나오더라ㅋㅋ
    # 문제를 끝까지 잘 읽자!!!
def Increase_Number():
    final_number = []
    nat_number = []
    for i in range(100, 1000):
        reverse_letter = ""
        str_i = str(i)
        for j in range(3):
            reverse_letter += str_i[-(j+1)]

        if int(str_i[2]) != 0:
            reverse_number = int(reverse_letter)
            mul_number = str(i * reverse_number)    # 123 * 321 = 39483
            if len(mul_number) == 5: # 5자리 일 때
                if mul_number[0] <= mul_number[1] and mul_number[1] <= mul_number[2] and mul_number[2] <= mul_number[3] and mul_number[3] <= mul_number[4]:
                    final_number.append(int(mul_number))
                    nat_number.append(i)
                else:
                    continue
            else: # 그 외, 6자리 일 때
                if mul_number[0] <= mul_number[1] and mul_number[1] <= mul_number[2] and mul_number[2] <= mul_number[3] and mul_number[3] <= mul_number[4] and mul_number[4] <= mul_number[5]:
                    final_number.append(int(mul_number))
                    nat_number.append(i)
                else:
                    continue

        else:
            continue


    print(nat_number)
    print(final_number)
    print(len(final_number))

Increase_Number()