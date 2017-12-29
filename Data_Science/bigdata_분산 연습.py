# 분산(Variance) 공식 : (제곱의 평균) - (평균의 제곱)")

a = [1,2,3,4,5,6,7,8,9,10]

b = 0
c = 0
for i in a:
    b += int(i)*int(i)
    c += int(i)

d = c/len(a)
print(b)            # 제곱의 합
print(b/len(a))     # 제곱의 평균
print(c*c)          # 합의 제곱
print(d*d)          # 평균의 제곱


# 분산(Variance) 공식 : (제곱의 평균) - (평균의 제곱)")
square_sum = 0
average_sum = 0
for i in row_instance:
    square_sum += float(i) * float(i)
    average_sum += float(i)

square_average = square_sum/len(row_instance)
average_square_first = average_sum/len(row_instance)
average_square = average_square_first * average_square_first

variance_row = square_average - average_square