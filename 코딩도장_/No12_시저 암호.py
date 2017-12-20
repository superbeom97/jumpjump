# 시저 암호
#
# 시저 암호는 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데
# 예를 들어 알파벳 A를 입력했을 때
# 그 알파벳의 n개 뒤에 오는(여기서는 예를 들 때 3으로 지정하였다)알파벳이 출력되는 것이다.
# 예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
#
# 어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라.


def Caesar():
    print("이 프로그램은 알파벳 입력시, 설정한 범위만큼 뒤의 알파벳으로 변환해 주는 시저 암호 프로그램입니다.")
    number = int(input("범위를 설정해 주세요: ")) # 3
    original_letter = input("바꾸고 싶은 단어를 입력해 주세요: ")  # "CAT"
    chage_letter = ""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # 0 ~ 25

    for i in range(len(original_letter)):
        find_alp = alphabet.index(original_letter[i]) + number
        if find_alp <= 25:
            chage_letter += alphabet[find_alp]
        else:
            find_alp = find_alp - 26 # Z + 3 = 28 -> 2로 만들어 줘야 해. 그래서 28 - 26!!
            chage_letter += alphabet[find_alp]

    print(chage_letter)

while True:
    Caesar()