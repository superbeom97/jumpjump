def getTotalPage(m, n):
    if m <= n:
        s = '1'
    elif m % n == 0:
        s = int(m / n)
    else:
        s = int((m / n) + 1)

    print("게시물 총 건 수: %s, 한 페이지에 보여줄 게시물 수: %s, 총 페이지 수: %s" % (m, n, s))


getTotalPage(5, 10)