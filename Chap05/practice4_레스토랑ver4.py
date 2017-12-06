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

    def set_number_serced(self, number):
        print("새로운 손님 %s명 들어오십니다." % number)

    def increment_number_served(self, number):
        print("오늘의 총 손님 수는 %s명입니다." % number)

A_restaurant = Restaurant("'복복복을 먹자'", "'대구 전통의 맛'")
A_restaurant.describe_restaurant()
A_restaurant.open_restaurant()
A_restaurant.set_number_serced(7)
A_restaurant.increment_number_served(52)