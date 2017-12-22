print("유쾌한 점퍼를 알아보고 싶은 수열을 입력하시오(첫 자리에는 개수를 입력하시오): ")
while True:
    original_jumper_str = input()
    original_jumper = original_jumper_str.split()
    range_check_jumper = original_jumper[0]

    check_jumper = []
    for i in range(1, len(original_jumper)):
        try:
            check_jumper.append(abs(int(original_jumper[i]) - int(original_jumper[i+1])))
        except:
            pass

    true_or_false = ""
    for j in (1, len(check_jumper)):
        if int(j) in check_jumper:
            true_or_false += "o"
        else:
            true_or_false += "x"

    if "x" in true_or_false:
        print("Not Jolly")
    else:
        print("Jolly")