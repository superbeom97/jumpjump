#################### 부정형 전방 탐색

import re

def check_match(p,file_name):
    m = p.match(file_name)
    if m:
        print(m)

# Step1] 파일명.확장자를 나타내는 정규식
file_name_candidates=["foo.bar","autoexec.bat","sendmail.cf"]

p = re.compile(".*[.].*$")

print("첫번째 정규식 테스트: .*[.].*$")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step2] 확장자가 bat 파일 제외
p = re.compile(".*[.][^b].*$")      ## 문자 클래스 [] 안에 있는 '^'는 반대(not)라는 의미
print("\n두번째 정규식 테스트: .*[.][^b].*$")        ## -> 하지만 확장자 bar 파일도 제외되는
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step3] 확장자가 bat 파일 제외 두번쨰 시도
p = re.compile(".*[.]([^b]..|.[^a].|..[^t])")       ## -> 하지만 확장자 cf 파일도 제외되는
print("\n세번째 정규식 테스트: .*[.]([^b]..|.[^a].|..[^t]")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step4] 확장자가 bat 파일 제외 세번쨰 시도
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)")
print("\n네번째 정규식 테스트: .*[.]([^b]..|.[^a].|..[^t]")
for file_name in file_name_candidates:
    check_match(p,file_name)

## 전방 탐색만으로는 코드가 점점 더러워져... 그래서 나온 게 부정형 전방 탐색
p = re.compile(".*[.](?!bat$).*$")      ## .bat 라는 문자열은 통과해라
print("\n부정형 전방 탐색 정규식 테스트: .*[.](?!bat$).*$")
for file_name in file_name_candidates:
    check_match(p,file_name)