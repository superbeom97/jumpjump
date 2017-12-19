def Nature_Number():
    nat_number = int(input("자연수를 입력하시오: "))
    div_number = 0
    # total_number = []

    for j in range(1, nat_number+1):
        for i in range(1, j+1):
            if j % i == 0:
                div_number += i
            else:
                continue

        pure_number = int(div_number / 2)
        if pure_number == nat_number:
            print(pure_number)

while True:
    Nature_Number()