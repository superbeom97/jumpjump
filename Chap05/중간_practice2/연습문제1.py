f = open("D:\Python_workspace\jumpjump\Chap05\\learning_python.txt", 'r')
data = f.read()
change = data.replace("python", "C")
# f.close()

f = open("D:\Python_workspace\jumpjump\Chap05\\learning_python_copyed.txt", 'w')
f.write(change)
f.close()