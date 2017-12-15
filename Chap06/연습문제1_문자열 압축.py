# 아직 미완성!!!!!!
while True:
    let = input("문자를 입력하세요: ") # "aaabbcccccca"
    let_list = list(let) # ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'a']

    i = 0
    for j in let_list:
        if let_list[j] == let_list[j+1]:
            b = let_list[j] + let_list[j+1]
            print(b)
        else:
            continue