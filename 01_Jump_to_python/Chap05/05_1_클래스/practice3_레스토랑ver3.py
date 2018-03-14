class Restaurant:
    cuisine_type = "대구 전통의 맛"
    restaurant_name = "복복복을 먹자"
    number_served = 0 # 이 변수, 어렵다!

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고, %s 전문점입니다." % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % self.restaurant_name)

    def set_number_served(self, number):
        self.number_served = number # 이 변수를 몰라서 못 넣었다! 추가해주는 거 잊지 말고~
        print("방문한 손님을 %s명으로 수정하였습니다." % self.number_served)

    def increment_number_served(self, number):
        self.number_served += number # 이 변수를 몰라서 못 넣었다! 추가해주는 거 잊지 말고~
        print("오늘의 총 손님 수는 %s명입니다." % self.number_served)


A_restaurant = Restaurant("'복복복을 먹자'", "'대구 전통의 맛'")
A_restaurant.describe_restaurant()
A_restaurant.open_restaurant()

A_restaurant.set_number_served(20)  # 손님 수를 임의로 설정해서 넣어 준 뒤
print(A_restaurant.number_served) # 확인하고 싶으면 이렇게 print 함수를 사용해서 확인!!
A_restaurant.increment_number_served(5)
print(A_restaurant.number_served) # 확인하고 싶으면 이렇게 print 함수를 사용해서 확인!!