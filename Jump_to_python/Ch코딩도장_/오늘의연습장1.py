def Same_Phone():
    T = U = V = 8
    W = X = Y = 9

    phone_number = int(input("비교하고 싶은 전화번호의 개수와 전화번호를 입력하시오: "))

    number_list_first = []
    for i in range(phone_number):
        i = input()
        number_list_first.append(i)

    number_list_second = []
    for j in number_list_first:
        change_j = j.replace("-", "")
        for z in change_j:
            if z == "A" or z == "B" or z == "C":
                change_number = change_j.replace("A", "2")
                change_number = change_j.replace("B", "2")
                change_number = change_j.replace("C", "2")
                number_list_second.append(change_number)
            elif z == "D" or z == "E" or z == "F":
                change_number = change_j.replace("D", "3")
                change_number = change_j.replace("E", "3")
                change_number = change_j.replace("F", "3")
                number_list_second.append(change_number)
            elif z == "G" or z == "H" or z == "I":
                change_number = change_j.replace("G", "4")
                change_number = change_j.replace("H", "4")
                change_number = change_j.replace("I", "4")
                number_list_second.append(change_number)
            elif z == "J" or z == "K" or z == "L":
                change_number = change_j.replace("J", "5")
                change_number = change_j.replace("K", "5")
                change_number = change_j.replace("L", "5")
                number_list_second.append(change_number)
            elif z == "M" or z == "N" or z == "O":
                change_number = change_j.replace("M", "6")
                change_number = change_j.replace("N", "6")
                change_number = change_j.replace("O", "6")
                number_list_second.append(change_number)
            elif z == "P" or z == "R" or z == "S":
                change_number = change_j.replace("P", "7")
                change_number = change_j.replace("R", "7")
                change_number = change_j.replace("S", "7")
                number_list_second.append(change_number)
            elif z == "T" or z == "U" or z == "V":
                change_number = change_j.replace("T", "8")
                change_number = change_j.replace("U", "8")
                change_number = change_j.replace("V", "8")
                number_list_second.append(change_number)
            elif z == "W" or z == "X" or z == "Y":
                change_number = change_j.replace("W", "9")
                change_number = change_j.replace("X", "9")
                change_number = change_j.replace("Y", "9")
                number_list_second.append(change_number)
            # else:
                # number_list_second.append(change_number)

    print(number_list_second)


Same_Phone()