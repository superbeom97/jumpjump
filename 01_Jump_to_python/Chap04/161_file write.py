f = open("D:\Camp\my file\here\새파일.txt", 'w') # 근데 파일 이름 중에 n이 있으면 \n이 함수로 들어가
                          # 안전빵으로 \를 하나씩 추가해 주는 게 좋아 D:\\Camp\\my file\\here\\새파일.txt
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


for i in range(1, 12):
    data = "%d번째 줄입니다." % i
    print(data)