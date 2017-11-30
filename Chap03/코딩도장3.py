# m = 게시물의 총 건수
# n = 한 페이지에 보여줄 게시물 수
# s = 출력될 총 페이지 수
while True:
    m = int(input("게시물의 총 건수를 입력하세요:"))
    if m < 0:
        print("올바른 게시물의 총 건수를 입력하세요")
        continue
    elif m ==0:
        n = int(input("한 페이지에 보여줄 게시물 수를 입력하세요:"))
        if n <= 0:
            print("올바른 게시물 수를 확인하세요")
            continue
        else:
            print('0')
            continue
    else:
        n = int(input("한 페이지에 보여줄 게시물 수를 입력하세요:"))
        if n <= 0:
            print("올바른 게시물 수를 확인하세요")
            continue
        else:
            if m <= n:
                print('1')
                continue
            elif m % n == 0:
                print(int(m/n))
                continue
            else:
                print(int((m/n)+1))

# m을 n으로 나눴을 때 ==0 이면 몫 그래로
# m을 n으로 나눴을 때 !=0 이면 몫+1

#  m 29 n 10 => s 3
# m 30 n 10 => s 3
# m 31 n 10 => s 4

# m 99 n 10 => 10
# m 100 n 10 => s 10
# m 102 n 10 => s 11
