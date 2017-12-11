while True:
    reason = str(input("프로그래밍이 왜 좋으세요? (프로그램 종료를 원하시면 '종료'를 입력해 주세요) : "))
    if reason != "종료":
        name = str(input("당신의 이름은 무엇입니까? "))
        if name != "":
            try:
                f = open("pol.txt", 'a')
            except FileNotFoundError:
                number = int(input("pol.txt. 파일이 없습니다. 아래 중 선택하세요\n1. 종료\n2. 변경된 파일 경로 입력\n: "))
                if number == 1:
                    break
                elif number == 2:
                    address = str(input("변경된 파일 경로를 입력하세요: "))
                else:
                    print("1번과 2번 중에 선택해라잉 확 마")
                    continue

            # f = open("D:\Python_workspace\jumpjump\Chap05\중간_practice\\pol.txt", 'a')
            # f.write("[" + name + "]")
            # f.write(" ")
            # f.write(reason)
            # f.write("\n")
            # f.close()
            print("설문에 응답해 주셔서 감사합니다.")

    elif reason == "종료":
        print("이용해 주셔서 감사합니다.")
        break