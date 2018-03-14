f = open("D:\\Python_workspace\\jumpjump\\Chap04\\방명록.txt", 'w')
data = "홍길동 800912\n손미나 901223\n"
f.write(data)
f.close()

while True:
    name = input("이름을 입력하세요: ")
    if name in data:
        print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요." % name)
        continue
    else:
        yymmdd = int(input("생년월일을 입력하세요 (예:801212): "))
        f = open("D:\\Python_workspace\\jumpjump\\Chap04\\방명록.txt", 'a')
        data = "%s %s\n" % (name, yymmdd)
        f.write(data)
        f.close()
        print("%s님 방문을 환영합니다. 즐거운 시간되세요" % name)
        continue