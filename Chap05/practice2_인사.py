person = 0

while True:
    name = str(input("안녕하세요:) 이름을 입력하세요: "))

    if name:
        person +=1

        if person >= 11:
            print("Sorry, %s. The event is closed because you are %sth person come here." % (name, person))

        elif 4 <= person <= 10:
            print("Hi %s!! You are %sth person come here!" %(name, person))

        elif person == 1:
            print("Hi %s!! You are %sst person come here!" % (name, person))

        elif person == 2:
            print("Hi %s!! You are %snd person come here!" % (name, person))

        elif person == 3:
            print("Hi %s!! You are %srd person come here!" % (name, person))