def sum_and_mul(a, b):
    return a+b
    return a*b  # return은 항상 하나만!

result = sum_and_mul(2, 3)
print(result)  # return문을 2번 사용하면, 2개의 결과값을 돌려주는 것이 아니라
               # 두 번째 return문인 return a*b는 실행 X