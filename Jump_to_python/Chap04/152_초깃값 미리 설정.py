def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself('전수범', 28)
say_myself('전수범', 28, True)

say_myself('전수진', 27, False)