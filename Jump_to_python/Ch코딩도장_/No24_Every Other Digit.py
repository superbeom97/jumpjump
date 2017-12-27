# Every Other Digit
#
# 모든 짝수번째 숫자를 * 로 치환하시오.
# (홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.)
# 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.
#
# Example: a1b2cde3~g45hi6 → a*b*cde*~g4*hi6

S = "a1b2cde3~g45hi6"
sort_S = list(S)


for i in range(len(S)):
    if (i+1) % 2 == 0:
        try:
            if type(int(sort_S[i])) is int:
                sort_S[i] = "*"
        except:
            pass
    else:
        continue

final_S = "".join(sort_S)

print(final_S)