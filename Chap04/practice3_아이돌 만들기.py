f = open("D:\Python_workspace\jumpjump\Chap04\연습생.txt", 'r')
show_list = f.read()
f.close()

make_idol = show_list.split('\n')
for i in make_idol:
    print("신예 아이돌 ", end="")
    print(i, end="")
    print(" 인기 급상승")


#for make_idol in show_list:
#    print("신예 아이돌 ", end="")
#    print(make_idol, end="")
#    print(" 인기 급상승")