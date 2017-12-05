import sys

args = sys.argv[1:]
for i in args:
    print("Hello, ", end="")
    print(i[0].upper() + i[1:] + '!')

# cmd 열어서 파일 있는 경로에서 -> python + 파일명 + 넣을 변수들
# D:\Python_workspace\jumpjump\Chap04>ptyhon greet_user.py janny hannah margot kevin min 하고 엔터 치면
#Hello, Janny!
#Hello, Hannah!
#Hello, Margot!
#Hello, Kevin!
#Hello, Min!             이렇게 출력된다.