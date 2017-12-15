def getTotalPage(m, n):
    # try:

    # except:
    #     pass

    if m <= n:
        s = '1'
        print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, s))

    if m % n == 0:
        s = int(m / n)
        print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, s))

    elif m > n:
        s = int((m / n) + 1)
        print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, s))


f = open("D:\Python_workspace\jumpjump\Chap06\\6장_practice\\condition.txt", 'r')
data = f.readlines()
# print(data[0])
# print(data)
for i in data:
    aa = i.split()
    m = aa[0]
    n = aa[1]
    getTotalPage(m, n)