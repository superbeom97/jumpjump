# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤
# 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고
# 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
# (예, 454 => 454, 4546793 => 454*67-9-3)
#
# DashInsert 함수를 완성하자.

# 입력 - 화면에서 숫자로 된 문자열을 입력받는다.
# "4546793"
#
# 출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
# "454*67-9-3"

def Letter_Number():
    letter = input("숫자를 연속하여 입력하시오: ")
    sum_letter = ""
    for i in range(len(letter)):
        try:
            if letter[i+1]:
                if int(letter[i]) % 2 == 0:
                    if int(letter[i+1]) % 2 == 0:
                        sum_letter += letter[i] + "*"
                    else:
                        sum_letter += letter[i]
                else:
                    if int(letter[i+1]) % 2 != 0:
                        sum_letter += letter[i] + "-"
                    else:
                        sum_letter += letter[i]
            else:
                continue

        except:
            sum_letter += letter[i]

    print(sum_letter)

while True:
    Letter_Number()