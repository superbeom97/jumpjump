# 자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
# 예를 들면, 6과 28은 완전수이다.
# 6=1+2+3 // 1,2,3은 각각 6의 약수
# 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수
#
# 입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.

## 약수 구하는 방법
# n = 28 이고, n의 약수를 x라고 하면
# x로 n을 나눴을 때 나머지가 0이 되면 x는 n의 약수


def Nature_Number():
    nat_number = int(input("완전수를 출력할 범위를 입력하시오: "))

    for j in range(1, nat_number+1):
        div_number = 0
        for i in range(1, j+1):
            if j % i == 0:
                div_number += i
            else:
                continue

        pure_number = int(div_number / 2)
        if pure_number == j:
            print(pure_number)

while True:
    Nature_Number()