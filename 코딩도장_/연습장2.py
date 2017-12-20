n = 1330 # 몫
rest = [] # 나머지
binary_number = ""

while True:
    if n != 0:
        rest.append(n % 2)
        n = n // 2

    else:
        for i in range(1, len(rest)+1):
            binary_number += str(rest[-i])

        print(binary_number)
        break