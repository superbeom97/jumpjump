### 출력에서, 전화번호 숫자에 따른 증가식 출력을 제외하고 완성
### 증가식 출력이 되도록 코딩해야 함!!!

def Check_Number(compa_num):
    two = 'ABC2'
    three = 'DEF3'
    four = 'GHI4'
    five = 'JKL5'
    six = 'MNO6'
    seven = 'PRS7'
    eight = 'TUV8'
    nine = 'WXY9'
    new_num = ''

    if compa_num == '1': new_num = '1'
    elif compa_num in two: new_num = '2'
    elif compa_num in three: new_num = '3'
    elif compa_num in four: new_num = '4'
    elif compa_num in five: new_num = '5'
    elif compa_num in six: new_num = '6'
    elif compa_num in seven: new_num = '7'
    elif compa_num in eight: new_num = '8'
    elif compa_num in nine: new_num = '9'
    elif compa_num == '0': new_num = '0'

    return new_num


range_num = int(input("비교하고 싶은 전화번호의 개수를 입력해 주세요(예, 12) : "))
print("\n<<비교하고 싶은 전화번호를 십진 숫자들과 대문자(Q,Z 제외), 하이픈(-)을 사용하여 입력해 주세요>>\n"
      "하이픈(-)을 제외한 숫자 또는 문자를 모두 7개 입력하셔야 합니다:)\n")
phone_num_ls = []   ## ls는 list 줄인 말 _범용    ## 입력 받은 전화번호가 저장되는 리스트
just_one_num_ls = []    ## 입력 받은 전화번호에서 하이픈 없애고, 하나의 문자열로 만들어진 전화번호가 저장되는 리스트
for ph_num in range(range_num):
    phone_number = input("비교하고 싶은 전화번호를 입력해 주세요(예, 751-2205 or 56-4-GOAL) : ")
    phone_num_ls.append(phone_number)

for compa in phone_num_ls:  ## compa는 comparison(비교) 줄인 말 _내 임의     (예, 758-21-5-1 입력)
    change_first = compa.split('-')     ## 전화번호를 하이픈(-) 기준으로 나눠라 -> 하이픈을 기준으로 리스트로 저장 (예, ['758', '21', '5', '1'])
    just_one_number = ""    ## 전화번호를 하이픈 없이 하나의 문자열로 저장할, 빈 문자열
    for change_second in change_first:  ## 리스트로 저장된 것들을 하나씩 change_second에 입력
        just_one_number += change_second    ## 문자열로 받은 전화번호들을 just_one_number에 더해라
                                            ## -> for문이 종료되면 전화번호는 하이픈 없이 하나의 연속된 문자열이 되는
    just_one_num_ls.append(just_one_number)

change_num_ls = []
for one_num in just_one_num_ls:
    change_number = ''
    num_count = 0
    for compa_num in one_num:
        num_count += 1
        change_number += Check_Number(compa_num)    ## chage_number = Check_Number 함수의 return 값이다
        if num_count == 3: change_number += '-'     ## 전화번호가 3개 써지고 나서 하이픈(-)을 넣는
    change_num_ls.append(change_number)

mul_count_ls = []
change_num_index = -1
for step_by in change_num_ls:
    mul_count = 1
    change_num_index += 1
    if len(step_by) == 8:
        if change_num_index == range_num - 1:   ## range_num -1 or len(change_num_ls) - 1
            mul_count_ls.append("%s     No duplicates" % step_by)
            break   ## z가 change_num_ls의 마지막 자릿 수 일 때는 비교 대상이 없으니, 종료해라
        del_index = 0
        for x in change_num_ls[(change_num_index+1):]:
            del_index += 1
            if step_by == x:
                mul_count += 1
                change_num_ls[del_index] = x + "%s" % del_index

        each_ls = []
        if mul_count > 1:
            each_ls.append("%s" % step_by)
            each_ls.append(mul_count)
            mul_count_ls.append(each_ls)
        elif mul_count == 1:
            each_ls.append("%s" % step_by)
            each_ls.append("No duplicates")
            mul_count_ls.append(each_ls)

print(mul_count_ls)
## >> [['123-4567', 2], ['987-6542', 'No duplicates'], ['456-8792', 'No duplicates'], ['321-5487', 'No duplicates']]
mul_count_ls.sort(key=lambda x: x[0])   ## 리스트 내에서 첫 번째 인덱스로 정렬해라
print(mul_count_ls)
## >> [['123-4567', 2], ['321-5487', 'No duplicates'], ['456-8792', 'No duplicates'], ['987-6542', 'No duplicates']]
print("")

for number_prn in mul_count_ls:
    print("%s       %s" % (number_prn[0], number_prn[1]))
print("")
mul_count_ls.sort(key=lambda x: x[0], reverse=True)     ## 리스트 내에서 첫 번째 인덱스로 내림차순 정렬해라
for number_prn in mul_count_ls:
    print("%s       %s" % (number_prn[0], number_prn[1]))


# 487-3229
#
# 회사원들은 외우기 좋은 전화번호를 갖고 싶어한다.
# 전화번호를 외우기 쉽도록 만드는 한 방법은 기억하기 좋은 단어나 구절이 되도록 하는 것이다.
# 예를 들어, 워털루 대학의 전화는 TUT-GLOP으로 전화를 걸 수 있다.
# 때때로 번호의 일부만이 단어를 쓰기 위해 사용될 수 있다.
# Gino에서 피자를 주문하기 위해 310-GINO로 전화를 거는 식이다.
# 전화번호를 외우기 좋도록 하는 또다른 방법은 숫자들을 기억하기 좋은 방법으로 묶는 것이다.
# 3-10-10-10 (Three-tens)으로 전화를 걸면 피자헛에 주문을 할 수 있다.
#
# 전화번호의 표준형은 세 번째 번호와 네 번째 번호 사이에 하이픈(-)을 삽입한 7개의 숫자로 구성되어 있다.
# (예: 888-1200). 전화기의 키패드는 다음과 같은 글자 대 숫자의 대응을 지닌다.
#
# A, B, C -> 2
# D, E, F -> 3
# G, H, I -> 4
# J, K, L -> 5
# M, N, O -> 6
# P, R, S -> 7
# T, U, V -> 8
# W, X, Y -> 9
# Q와 Z에 대한 대응관계는 존재하지 않는다. 하이픈은 전화기에 입력되지 않으며 필요에 따라 추가되거나 빠질 수 있다.
# TUT-GLOP의 표준형은 888-4567이고, 310-GINO의 표준형은 310-4466, 3-10-10-10의 표준형은 310-1010이다.
#
# 만약 어떤 두 전화번호가 같은 표준형을 지니면 그들은 같은 번호이다.
#
# 여러분의 회사는 지역 회사원들의 전화번호를 정리하고 있다.
# 품질 관리 과정의 일환으로, 여러분은 정리된 전화번호부의 번호 중에 같은 것이 둘 이상 있지 않은지 확인하고 싶다.
#
# Input
#
# 입력은 하나의 테스트 케이스로 구성된다. 입력의 첫 줄은 전화번호의 갯수(<=100,000)로 이뤄져 있다.
# 남은 줄들은 전화번호부 내의 전화번호들이 한 줄에 하나씩 들어 있다.
# 각 전화번호는 십진 숫자들과 대문자(Q,Z 제외), 하이픈으로 구성된 문자열로 이뤄져 있다.
# 문자열 내에서 정확히 7개의 문자들이 숫자 또는 알파벳 문자이다.
#
# Output
#
# 한 번 이상 등장한 전화번호들이 출력을 구성한다.
# 각 줄은 표준형으로 표현된 전화번호와 출현 횟수가 하나의 공백 문자로 구분되어 있다.
# 출력되는 전화 번호들은 증가하는 사전식 순서로 되어 있어야 한다.
# 만약 입력으로 들어온 전화번호 중에 중복이 없다면 "No duplicates."를 출력한다.
#
# <<Sample Input>>
# 12
# 4873279
# ITS-EASY
# 888-4567
# 3-10-10-10
# 888-GLOP
# TUT-GLOP
# 967-11-11
# 310-GINO
# F101010
# 888-1200
# -4-8-7-3-2-7-9-
# 487-3279
#
# <<Sample Output>>
# 310-1010 2
# 487-3279 4
# 888-4567 3