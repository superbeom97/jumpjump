f = open("D:\\Python_workspace\\jumpjump\\Chap04\\연습생.txt", 'r')
show_list = f.read()
print(show_list, "\n")
f.close()

make_idol = show_list.split() # split 개념을 생각하지 못했었다. f.read()로 불렀으니 하나의 문자열이야
for i in make_idol:          # 그걸 하나하나 나눠 주기 위해 split 사용!!
    print("신예 아이돌 " + i + " 인기 급상승")
print("\n", end="")

make_world_star = show_list.split()
for j in make_world_star:
    print("아이돌 " + j + " 월드스타 등극")