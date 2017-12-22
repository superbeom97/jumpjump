# Jolly Jumpers
#
# n개의 정수(n>0)로 이루어진 수열에 대해 서로 인접해 있는 두 수의 차가 1에서 n-1까지의 값을 모두 가지면
# 그 수열을 유쾌한 점퍼(jolly jumper)라고 부른다.
# 예를 들어 다음과 같은 수열에서
# 1 4 2 3
# 앞 뒤에 있는 숫자 차의 절대 값이 각각 3,2,1이므로 이 수열은 유쾌한 점퍼가 된다.
#
# 어떤 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.
#
# <<Input>>
# 각 줄 맨 앞에는 3000 이하의 정수가 있으며 그 뒤에는 수열을 나타내는 n개의 정수가 입력된다.
# 맨 앞 숫자가 0이면 출력하고 종료한다.
#
# <<output>>
# 입력된 각 줄에 대해 "Jolly" 또는 "Not Jolly"를 한 줄씩 출력한다
#
# <<Sample Input>>
# 4 1 4 2 3
# 5 1 4 2 -1 6
#
#
# 주의: 각 줄의 맨 앞의 숫자는 수열의 갯수이다.
# 첫번째 입력인 4 1 4 2 3 의 맨 앞의 4는 뒤에 4개의 숫자가 온다는 것을 의미함
#
# <<Sample Output>>
# Jolly
# Not jolly


print("유쾌한 점퍼를 알아보고 싶은 수열을 입력하시오(첫 자리에는 개수를 입력하시오): ")
total_jumper = []
while True:
    original_jumper_str = input()
    original_jumper = original_jumper_str.split()
    range_check_jumper = int(original_jumper[0])

    if range_check_jumper != 0:
        check_jumper = []
        for i in range(1, len(original_jumper)):
            try:
                check_jumper.append(abs(int(original_jumper[i]) - int(original_jumper[i+1])))
            except:
                pass

        true_or_false = ""
        for j in range(1, len(check_jumper)+1):
            if int(j) in check_jumper:
                true_or_false += "o"
            else:
                true_or_false += "x"

        if "x" in true_or_false:
            total_jumper.append("Not Jolly")
        else:
            total_jumper.append("Jolly")

    elif range_check_jumper == 0:
        for z in total_jumper:
            print(z)
        break