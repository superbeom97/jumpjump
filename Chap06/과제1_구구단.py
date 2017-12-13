def GuGu(number):
    result = []
    for i in range(1, 10):
        i = i*number
        result.append(i)
    return result


print(GuGu(2))
