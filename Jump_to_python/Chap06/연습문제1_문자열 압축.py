def letter():
    let = input("문자를 입력하세요: ")
    blank_let = ""
    result = ""
    count = 0

    for i in let:
        if i != blank_let:
            blank_let = i
            count = 1
            result = result + blank_let + str(count)

        else:
            count += 1
            result = result + "\b" + str(count)

    return  result

while True:
    print(letter())