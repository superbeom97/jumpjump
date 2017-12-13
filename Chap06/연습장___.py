while True:
    let = input("문자를 입력하세요: ") # "aaabbcccccca"
    let_list = list(let) # ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'a']

    i = 0
    result = []
    for j in let_list:
        print(j)
        # if let_list[j] == let_list[j+1]:
        #     b = let_list[j] + let_list[j+1]
        #     result = result.append(b)
        # else:
        #     continue




# let = "aaabbcccccca"
# let_list = list(let)
# print(let)
# print(let_list)
# print(let_list[0]+let_list[1])