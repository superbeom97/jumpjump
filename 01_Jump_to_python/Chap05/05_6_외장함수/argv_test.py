# pickle
import pickle
f = open("test.txt", 'wb')
data = {1:'python',2:'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

## 파일 생성할 때
f = open("test.txt", 'w') # f = open("D:\Python_workspace\jumpjump\Chap05\05_6_외장함수\\test.txt.") 처럼
data = "즐거운 나날"      # 주소를 일일이 적을 필요 없이 그냥 파일 이름만 적어서 만들어도
f.write(data)             # 현재 열려있는 py가 속해 있는 폴더 내에 생성된다.
f.close()


# OS 모듈
import os
print(os.getcwd()) # 현재 디렉터리 위치를 리턴

os.system("dir") # 시스템 자체의 프로그램이나 기타 명령어를 호출

f = os.popen("dir") # 시스템 명령어를 실행시킨 결과값을 읽기 모드 형태의 파일 객체로 리턴
print(f.read()) # 읽어 들인 파일 객체의 내용을 보기 위해서


import os
os.mkdir("05_test_directory") # 05_6_외장함수 디렉터리 하위에 05_test_directory 디렉터리 생성
os.rmdir("05_test_directory") # 05_6_외장함수 디렉터리 하위에 05_test_directory 디렉터리 삭제

