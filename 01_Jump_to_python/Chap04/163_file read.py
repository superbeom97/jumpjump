f = open("D:\Camp\my file\here\새파일.txt", 'r') # 가장 첫 번째 줄이 화면에 출력
line = f.readline()
print(line)
f.close()

f = open("D:\Camp\my file\here\새파일.txt", 'r') # 모든 라인을 읽어서 화면에 출력
while True:
    line = f.readline()
    if not line: break
    print(line) # 하지만, 파일에 엔터가 자동으로 들어가 있어 그래서 화면에 출력하면
f.close()       # 엔터 + 여기서의 엔터 때문에 한 줄씩 더 띄워져

f = open("D:\Camp\my file\here\새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line, end="") # 그래서 붙여주기 위해 end="" 를 넣어주는
f.close()