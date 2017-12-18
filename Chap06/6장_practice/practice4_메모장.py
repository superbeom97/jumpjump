import sys

args = sys.argv
args_one = args[1]
args_two = args[2:]

if args_one == "-a":
    try:
        f = open("memo.txt", 'a')
        f.write(" ".join(args_two))
        f.write("\n")
        f.close()

    except FileNotFoundError:
        number = int(input("memo.txt 파일이 없습니다. 아래 중 선택하세요\n1. memo.txt 파일을 새로 생성하시겠습니까?\n2. 파일 경로를 입력하시겠습니까?\n: "))

        if number == 1:
            f = open("memo.txt", 'w')
            f.write(" ".join(args_two))
            f.write("\n")
            print("memo.txt 파일을 생성했습니다. 감사합니다.")
            f.close()

        elif number == 2:
            address = str(input("파일 경로를 입력하세요: "))
            f = open(address, 'a')
            f.write(" ".join(args_two))
            f.write("\n")
            f.close()
            print("정상 처리되었습니다. 감사합니다.")

        else:
            print("1번과 2번 중에 선택해라잉 확 마")

elif args_one == "-au":
    for i in args_two:
        f = open("memo.txt", 'a')
        b = "".join(i)
        # f.write("\n")
        # print(i.upper(), end=" ")
        f.write(b.upper()+"\n")
        f.close

elif args_one == "-v":
    try:
        f = open("memo.txt", 'r')

    except FileNotFoundError:
        number = int(input("memo.txt 파일이 없습니다. bb아래 중 선택하세요\n1. 종료하시겠습니까?\n2. 파일 경로를 입력하시겠습니까?\n: "))

        if number == 1:
            print("이용해 주셔서 감사합니다.")
            # break

        elif number == 2:
            address = str(input("파일 경로를 입력하세요: "))
            print("정상 처리되었습니다. 감사합니다.")

        else:
            print("1번과 2번 중에 선택해라잉 확 마")