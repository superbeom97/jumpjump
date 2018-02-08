# 지뢰찾기
#
# 지뢰찾기 게임은 M x N 매트릭스에 위치해 있는 지뢰를 찾는 게임이다.
# M x N 매트릭스 상의 격자(square)는 지뢰이거나 지뢰가 아니다.
#
# 지뢰 격자는 *로 표시한다.
# 지뢰가 아닌 격자(square)는 숫자로 표시하며 그 숫자는 인접해 있는 지뢰의 수를 의미한다.
# (격자(sqaure)는 최대 8개의 인접한 지뢰를 가질 수 있다.)
#
# 다음은 4x4 매트릭스에서 2개의 지뢰(*)를 표시하는 방법이다.
# *...
# ....
# .*..
# ....
#
# 이 게임의 목표는 지뢰의 위치(*)를 제외한 나머지 격자들의 숫자를 맞추는 것이다.
#
# 위 경우의 답은 아래와 같다.
# *100
# 2210
# 1*10
# 1110

# <<입력>>
# 첫번째 줄은 M x N 의 M(행)과 N(열)에 해당되는 숫자이다. N과 M은 0보다 크고 100 이하이다. (0< N, M <=100)
# 그 다음 M개의 줄이 차례로 입력되고 각 줄은 정확하게 N개의 문자가 입력된다.
# 지뢰 격자는 *로 표시하며 // 지뢰가 아닌 격자는 .(dot)로 표시한다.
#
# <<출력>>
# 지뢰(*)를 제외한 나머지 격자의 숫자값을 찾아서 M x N 매트릭스를 출력한다.

# 예1)
# <<입력>>
# 4 4
# *...
# ....
# .*..
# ....
#
# <<출력>>
# *100
# 2210
# 1*10
# 1110
#
# 예2)
# <<입력>>
# 3 5
# **...
# .....
# .*...
#
# <<출력>>
# **100
# 33200
# 1*100


## Ver.1
mine_square_range = input("M x N 매트리스의 지뢰찾기 게임입니다. 매트리스 범위 M과 N을 설정해 주세요: ")
mine_square_split = mine_square_range.split()
M = mine_square_split[0]
N = mine_square_split[1]

mine_square_letter_group = ""
print("지뢰는 '*', 그 외는 '.'으로 입력하시오")
for i in range(int(M)):
    mine_square = input()
    mine_square_letter_group += mine_square

mine_square_number_group = ""
for i in mine_square_letter_group:
    mine_square_number = 0
    if i != "*":
        try:
            if mine_square_letter_group[i+5] == "*":
                mine_square_number += 1
            else: continue

            if mine_square_letter_group[i+4] == "*":
                mine_square_number += 1
            if mine_square_letter_group[i+3] == "*":
                mine_square_number += 1
            if mine_square_letter_group[i+1] == "*":
                mine_square_number += 1
            if mine_square_letter_group[i-1] == "*":
                mine_square_number += 1
            if mine_square_letter_group[i-3] == "*":
                mine_square_number += 1
            if mine_square_letter_group[i-4] == "*":
                mine_square_number += 1
            if mine_square_letter_group[i-5] == "*":
                mine_square_number += 1

            mine_square_number_group += ""

        except:
            pass



    else:
        mine_square_number_group += i


## Ver.2
def Mine_Square():
    range_number = [-5, -4, -3, -1, 1, 3, 4, 5]
    for z in range_number(len(mine_square_letter_group)):
        for j in range_number:
            if 0 < (z - j) <= int(M) * int(N):
                if mine_square_letter_group[z - j] == "*":
                    mine_square_number += 1
                else:
                    continue
            else:
                continue


mine_square_range = input("M x N 매트리스의 지뢰찾기 게임입니다. 매트리스 범위 M과 N을 설정해 주세요: ")
mine_square_split = mine_square_range.split()
M = mine_square_split[0]
N = mine_square_split[1]

mine_square_letter_group = ""
print("지뢰는 '*', 그 외는 '.'으로 입력하시오")
for i in range(int(M)):
    mine_square = input()
    mine_square_letter_group += mine_square

mine_square_number_group = ""
for i in mine_square_letter_group:
    mine_square_number = 0
    if i == "*":
        mine_square_number_group += i
    else:
        Mine_Square()
        mine_square_number_group += mine_square_number

print(mine_square_number_group)


## Ver.3
mine_square_range = input("M x N 매트리스의 지뢰찾기 게임입니다. 매트리스 범위 M과 N을 설정해 주세요: ")
mine_square_split = mine_square_range.split()
M = mine_square_split[0]
N = mine_square_split[1]

mine_square_letter_group = ""
print("지뢰는 '*', 그 외는 '.'으로 입력하시오")
for i in range(int(M)):
    mine_square = input()
    mine_square_letter_group += mine_square



def Mine_Square():
    mine_square_number_group = ""
    mine_square_number = 0
    range_number = [-5, -4, -3, -1, 1, 3, 4, 5]

    if i == "*":
        mine_square_number_group += i

    else:
        for z in range_number(len(mine_square_letter_group)):
            for j in range_number:
                if 0 < (z - j) <= int(M) * int(N):
                    if mine_square_letter_group[z - j] == "*":
                        mine_square_number += 1
                    else:
                        continue
                else:
                    continue
    mine_square_number_group += mine_square_number

for i in mine_square_letter_group:
    Mine_Square()


print(mine_square_number_group)