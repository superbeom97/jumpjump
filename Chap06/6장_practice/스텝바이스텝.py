def getTotalPage(m, n):
    try:
        if m <= n:
            s = '1'
        elif m % n == 0:
            s = int(m / n)
        else:
            s = int((m / n) + 1)

        print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, s))

    except:
        pass





f = open("D:\Python_workspace\jumpjump\Chap06\\6장_practice\\condition.txt", 'r')
data = f.read()
make_data = data.split()
m = [make_data[0], make_data[2], make_data[4], make_data[6], make_data[8]]
n = [make_data[1], make_data[3], make_data[5], make_data[7], make_data[9]]
# print(data)
# print(make_data)
# print(m)
# print(n)
for i in m:
    print(i)
for j in n:
    print(j)

    # getTotalPage(i, j)