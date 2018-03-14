# 파일찾기
#
# A라는 디렉토리 하위에 있는 텍스트 파일(*.txt) 중에서
# LIFE IS TOO SHORT 라는 문자열을 포함하고 있는 파일들을 모두 찾을 수 있는 프로그램을 작성하시오.
#
# 단, 하위 디렉토리도 포함해서 검색해야 함.

import os

txt_path = ""
for (path, dir, files) in os.walk("D:\Python_workspace\jumpjump/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            txt_path += "%s/%s " % (path, filename)

sort_txt_path = txt_path.split()

for i in sort_txt_path:
    f = open("%s" % i, 'r')
    data = f.read()
    if "LIFE IS TOO SHORT" in data:
        print("'D의 디렉토리 하위에 있는 텍스트 파일 중 'LIFE IS TOO SHORT'를 포함하고 있는 파일명은 다음과 같습니다'")
        print(">>" + i)
        print("'%s의 파일 내용은 다음과 같습니다'" % i)
        print(">>" + data + "\n")