def getTotalPage(m, n):
    try:
        if int(m) <= int(n):
            s = '1'
            print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, s))

        if int(m) % int(n) == 0:
            s = int(m) / int(n)
            print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, int(s)))

        elif int(m) > int(n):
            s = int(m) / int(n) + 1
            print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, int(s)))
    except:
        pass






f = open("D:\Python_workspace\jumpjump\Chap06\\6장_practice\\condition.txt", 'r')
for i in f.readlines():
    aa = i.split()
    m = aa[0]
    n = aa[1]
    getTotalPage(m, n)