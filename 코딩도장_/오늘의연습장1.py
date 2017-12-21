n = 22
add_number = []
add_number.append(n)
while True:
    if n != 1:
        if n % 2 == 0:
            n = n / 2
            add_number.append(int(n))
        else:
            n = (n * 3) + 1
            add_number.append(int(n))
    else:
        print(add_number)
        print(len(add_number))
        break