f = open("D:\Python_workspace\jumpjump\Chap04\연습생.txt", 'r')
show_list = f.read()
print(show_list, "\n")
f.close()

make_idol = show_list.split()
for i in make_idol:
    print("신예 아이돌 " + i + " 인기 급상승")
print("\n", end="")

make_world_star = show_list.split()
for j in make_world_star:
    print("아이돌 " + j + " 월드스타 등극")