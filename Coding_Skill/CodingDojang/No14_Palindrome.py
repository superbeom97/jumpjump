# palindrome

# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?


def Palindrome():
    final_number = 0
    for i in range(100, 1000):          # 100 x 100 = 10,000 -> 5자리 수
        for j in range(100, 1000):      # 999 x 999 = 998,001 -> 6자리 수
            mul_number = str(i * j)
            if len(mul_number) == 5: # 5자리 일 때
                if mul_number[0] == mul_number[4] and mul_number[1] == mul_number[3]:
                    if int(mul_number) > final_number:
                        final_number = int(mul_number)
                    else:
                        continue
                else:
                    continue
            else: # 그 외, 6자리 일 때
                if mul_number[0] == mul_number[5] and mul_number[1] == mul_number[4] and mul_number[2] == mul_number[3]:
                    if int(mul_number) > final_number:
                        final_number = int(mul_number)
                    else:
                        continue
                else:
                    continue

    print(final_number)

Palindrome()