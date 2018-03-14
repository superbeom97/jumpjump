f = open("D:\Camp\my file\here\새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close() # 화면에는 출력이 되지 않지만, 파일을 열어보면 추가가 되어 있다.