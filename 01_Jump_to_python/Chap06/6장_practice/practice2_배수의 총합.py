def Mul(rrange, one, two):
    print("0부터 %s이하의 범위를 선택하셨습니다. 이 중에서" % rrange)

    one_total_result = []
    one_result = ""
    sum_one_result = 0
    for i in range(1, rrange+1):
        if i % one == 0:
            one_total_result = one_total_result + [i]
            xx_one_result = one_result + str(i)
            one_result = one_result + str(i) + ","
            sum_one_result += i
        else:
            continue
    print("%s의 배수는 %s입니다." % (one, xx_one_result))

    two_total_result = []
    two_result = ""
    sum_two_result = 0
    for j in range(1, rrange+1):
        if j % two == 0:
            two_total_result = two_total_result + [j]
            xx_two_result = two_result + str(j)
            two_result = two_result + str(j) + ","
            sum_two_result += j
        else:
            continue
    print("%s의 배수는 %s입니다." % (two, xx_two_result))

    z_total_result = []
    z_result = ""
    sum_z_result = 0
    for z in range(1, rrange+1):
        if z % (one*two) == 0:
            z_total_result = z_total_result + [z]
            xx_z_result = z_result + str(z)
            z_result = z_result + str(z) + ","
            sum_z_result += z
        else:
            continue

    aa = set(one_total_result) | set(two_total_result)
    bb = list(aa)
    bb.sort()
    cc = ""
    for u in bb:
        dd = cc + str(u)
        cc = cc + str(u) + ","
    print("%s, %s의 배수는 %s입니다." % (one, two, dd))

    sum_total = 0
    for t in range(1, rrange+1):
        if t in aa:
            sum_total += t
        else:
            continue
    print("따라서 0부터 %s이하의 범위 내에서 %s, %s의 배수의 총합은 %s입니다." % (rrange, one, two, sum_total))


while True:
    number = input("<<'범위, 첫 번째 수, 두 번째 수'를 입력하세요.\n종료를 원하시면 '종료'를 입력하세요>> : ")
    john = "".join(number)
    check = john.split()

    finish = check[0]

    if finish == "종료":
        print("이용해 주셔서 감사합니다.")
        break

    else:
        john = "".join(number)
        check = john.split()

        rrange = int(check[0])
        one = int(check[1])
        two = int(check[2])

        Mul(rrange, one, two)