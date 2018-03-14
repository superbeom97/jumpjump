def input_number():
    number = input("숫자를 입력하시오: ")
    a = number.split() # -> ['0123456789', '01123']

    zero = "0"
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"

    for i in a:
        i = sorted(i)
        if i[0] == zero and i[1] == one and i[2] == two and i[3] == three and i[4] == four and i[5] == five and i[6] == six and i[7] == seven and i[8] == eight and i[9] == nine:
            print(True, end=" ")
        else:
            print(False, end=" ")
    print("\n")

while True:
    input_number()