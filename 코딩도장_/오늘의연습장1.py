def Binary_Number():
    number = int(input("2진법으로 나타내고 싶은 자연수를 입력하시오: ")) # 몫
    rest = []  # 나머지
    binary_number = ""

    while True:
        if number != 0:
            rest.append(number % 2)
            number = number // 2

        else:
            for i in range(1, len(rest) + 1):
                binary_number += str(rest[-i])

            print(binary_number)
            break

while True:
    Binary_Number()