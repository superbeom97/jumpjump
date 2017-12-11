f = open("D:\Python_workspace\jumpjump\Chap05\\poll.txt", 'w')
while True:
    reason = str(input("프로그래밍이 왜 좋으세요? (프로그램 종료를 원하시면 '종료'를 입력해 주세요) : "))
    if reason != "종료":
        name = str(input("당신의 이름은 무엇입니까? "))
        if name:
            f = open("D:\Python_workspace\jumpjump\Chap05\\poll.txt", 'a')
            f.write("[" + name + "]")
            f.write(" ")
            f.write(reason)
            f.write("\n")
            f.close()
            print("설문에 응답해 주셔서 감사합니다.")

    elif reason == "종료":
        print("이용해 주셔서 감사합니다.")
        break