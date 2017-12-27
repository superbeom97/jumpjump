f = open("D:\Camp\my file\here\새파일.txt", 'r')  # 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴
lines = f.readlines()
print(lines)
f.close()

f = open("D:\Camp\my file\here\새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()

f = open("D:\Camp\my file\here\새파일.txt", 'r')
print(f.read())
f.close()