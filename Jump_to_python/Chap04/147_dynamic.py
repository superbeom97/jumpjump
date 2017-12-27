def sum_many(*args):
    sum = 0

    for i in args:
        sum = sum + i

    return sum

result = sum_many(1, 2, 3)
print(result)
print(sum_many(1, 2, 3)) #위에 있는 두 줄을 한 줄로 축약해서 바로 적은 것

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)