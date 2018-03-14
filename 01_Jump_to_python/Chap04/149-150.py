def sum_and_mul(a, b):
    return a+b, a*b

result = sum_and_mul(3, 4) # 하나의 튜플로
print(result)

sum, mul = sum_and_mul(3, 4) # 2개의 결과값으로 받고 싶다면
print(sum)
print(mul)