f = open("D:\Camp\my file\here\새파일.txt", 'r')
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