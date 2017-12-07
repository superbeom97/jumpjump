#f = open("D:\\Python_workspace\\jumpjump\\Chap05\\고객서빙현황로그.txt", 'w')
#f.close()


class Restaurant:
    cuisine_type = "대구 전통의 맛"
    restaurant_name = "복복복을 먹자"
    number_served = 0

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고, %s 전문점입니다." % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % self.restaurant_name)

    def set_number_served(self, number):
        self.number_served = number
        print("방문한 손님을 %s명으로 수정하였습니다." % self.number_served)

    def increment_number_served(self, number):
        self.number_served += number
        print("오늘의 총 손님 수는 %s명입니다." % self.number_served)

    def __del__(self):
        print("이용해 주셔서 감사감사요~")


A_restaurant = Restaurant("'복복복을 먹자'", "'대구 전통의 맛'")
A_restaurant.describe_restaurant()
A_restaurant.open_restaurant()

#A_restaurant.set_number_served(30)
#print(A_restaurant.number_served)
A_restaurant.increment_number_served(50)
#print(A_restaurant.number_served)


f = open("D:\\Python_workspace\\jumpjump\\Chap05\\고객서빙현황로그.txt", 'r')
data = f.read() # f.read()로 읽었으니 하나의 문자열이야.
#print(data, "\n")
f.close()

make_data = data.split() # 문자열 함수 split을 사용해 각각 나눠주면 리스트 안에 들어가게 돼
#print(make_data)

f = open("D:\\Python_workspace\\jumpjump\\Chap05\\고객서빙현황로그.txt", 'a')
total = "\n%s" % (int(make_data[-1])+A_restaurant.number_served) # 리스트의 마지막 값을 정수화해서 더해주는
#print(total)
f.write(total)
f.close()

# a = f.read()로 불러오면 문자열이 돼 -> 이걸 어떻게 나눌 것인가? -> list(a) 사용하면 스튜핏!
# b = a.split() 함수를 사용해 주면 -> 리스트로 저장되는 -> b는 리스트형이 되는 거야!
# split() 함수를 사용하여! 문자열을 나누자!!