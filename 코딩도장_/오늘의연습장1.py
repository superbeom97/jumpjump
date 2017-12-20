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