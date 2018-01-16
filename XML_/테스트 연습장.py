a = ['서울특별시','대구광역시','울산광역시','서울 중구']

b= [i[0]+i[1]+i[2] for i in a ]

print(b.count("서울특"))
print(b.count("대구광"))