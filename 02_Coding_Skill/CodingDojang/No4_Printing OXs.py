# input은 int n을 입력 받아
# 첫번째 row는 (n-1)의 O와 X
# 두번째 row는 (n-2)의 O와 XX
# 세번째 row는 (n-3)의 0와 XXX
# ...
# n번째 row는 n의 X을 출력하시오
#
# 입력 예시: 6
#
# 출력 예시:
# OOOOOX
# OOOOXX
# OOOXXX
# OOXXXX
# OXXXXX
# XXXXXX

# Ver.1
def Num_OX():
    number_ox = int(input("프린트 할 OX의 총 개수 입력하시오: "))
    for i in range(1, number_ox+1):
        print((number_ox-i)*'O'+i*'X')

Num_OX()


# Ver.2
def Num_OX():
    number_ox = int(input("프린트 할 OX의 총 개수 입력하시오: "))
    for i in range(1, number_ox+1):
        number_o = (number_ox-i)*'O'
        number_x = i*'X'
        print(number_o+number_x)

Num_OX()