# A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
#
# 버전은 다음처럼 "." 으로 구분된 문자열이다.
#
# 버전 예) 1.0.0, 1.0.23, 1.1
#
# 두 개의 버전을 비교하는 프로그램을 작성하시오.
#
# 다음은 버전 비교의 예이다.

# 0.0.2 > 0.0.1
# 1.0.10 > 1.0.3
# 1.2.0 > 1.1.99
# 1.1 > 1.0.1

def Version():
    version = input("비교할 두 개의 버전을 입력하시오: ")
    version_list = version.split()

    one_version = version_list[0]
    one_version_list = one_version.split(".")

    two_version = version_list[1]
    two_version_list = two_version.split(".")

    for i in range(len(one_version_list)):
        if one_version_list[i] == two_version_list[i]:
            continue
        else:
            if one_version_list[i] > two_version_list[i]:
                print("%s > %s" % (one_version, two_version))
                break
            else:
                print("%s < %s" % (one_version, two_version))
                break

while True:
    Version()