# 넥슨 입사문제 중에서
#
# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# 예를 들어
# d(91) = 9 + 1 + 91 = 101
# 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
#
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며
# 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
#
# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.


## 처음에 푼 코드
def Self_Number():
    generator = []
    real_generator = []
    no_generator = []
    self_number = 0

    for i in range(1, 5001):
        letter_i = str(i)

        if len(letter_i) == 1:
            i = i * 2
            generator.append(i)

        elif len(letter_i) == 2:
            i = int(letter_i[0]) + int(letter_i[1]) + i
            generator.append(i)

        elif len(letter_i) == 3:
            i = int(letter_i[0]) + int(letter_i[1]) + int(letter_i[2]) + i
            generator.append(i)

        elif len(letter_i) == 4:
            i = int(letter_i[0]) + int(letter_i[1]) + int(letter_i[2]) + int(letter_i[3]) + i
            generator.append(i)

    for j in generator:
        if j < 5000:
            real_generator.append(j)
        else:
            continue

    for z in range(1, 5000):
        no_generator.append(z)

    self_number_group = set(no_generator) - set(real_generator)

    for x in self_number_group:
        self_number += x

    print(self_number)


Self_Number()


### 풀이 보고 한 수 배운 뒤,
## Ver.1 sum 함수를 이용하여 바로 더한
generator_group = []
for i in range(1, 5000): # 123
    generator_factor = 0
    for j in str(i): # 입력 받은 i를 문자열로 만들어 준 후, 하나씩 j에 넣는 거야. 그걸 int로 더하면
        generator_factor += int(j) # 각 자리 수를 더한 거야 -> 풀이 보고 배운 내용!!
    generator_group.append((generator_factor+int(i))) # 각 자리 수 더한 거 + 원래 입력 받은 수 = 제너레이터

total_group = []
for z in range(1, 5000):
    total_group.append(int(z))

self_number_group = set(total_group) - set(generator_group) # 1~4999에서 제너레이터 제외한 수들
sum_self_number = 0
for x in self_number_group:
    sum_self_number += int(x)
print(sum_self_number)


## Ver.2 sum 함수를 이용하여 바로 더한
generator_group = []
for i in range(1, 5000): # 123
    generator_factor = 0
    for j in str(i): # 입력 받은 i를 문자열로 만들어 준 후, 하나씩 j에 넣는 거야. 그걸 int로 더하면
        generator_factor += int(j) # 각 자리 수를 더한 거야!
    generator_group.append((generator_factor+int(i))) # 각 자리 수 더한 거 + 원래 입력 받은 수 = 제너레이터

total_group = []
for z in range(1, 5000):
    total_group.append(int(z))

self_number_group = set(total_group) - set(generator_group) # 1~4999에서 제너레이터 제외한 수들
print(sum(self_number_group))
# sum()은 정수형으로 저장되어 있는 수들을 더해 주는
# 예) a = [1,2,3]
# print(sum(a)) -> 1 + 2 + 3 = 6 이 된다.