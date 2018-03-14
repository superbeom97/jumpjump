# ver2.1
class Restaurant:
    cuisine_type = "대구 전통의 맛"
    restaurant_name = "복복복을 먹자"

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s 이고, %s 전문점입니다." % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % self.restaurant_name)


A_restaurant = Restaurant("'복복복을 먹자'", "'대구 전통의 맛'")
A_restaurant.describe_restaurant()
A_restaurant.open_restaurant()

B_restaurant = Restaurant("'우리가 진짜 맛집'", "'전통사찰음식'")
B_restaurant.describe_restaurant()
B_restaurant.open_restaurant()

C_restaurant = Restaurant("'엔지니어 기사 식당'", "'파이썬 코딩'")
C_restaurant.describe_restaurant()
C_restaurant.open_restaurant()


# ver2.2
class Restaurant:
    cuisine_type = "대구전통의맛"
#    restaurant_name = ""

    def __init__(self, name):
        self.restaurant_name = name

    def restaurant(self, cuisine):
        print("저희 레스토랑 명칭은 %s 이고, %s 전문점입니다." % (self.restaurant_name, cuisine))

    def open(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % self.restaurant_name)

A_restaurant = Restaurant("'복복복을 먹자'")
A_restaurant.open()
A_restaurant.restaurant("'대구 전통의 맛'")

B_restaurant = Restaurant("'우리가 진짜 맛집'")
B_restaurant.open()
B_restaurant.restaurant("'전통사찰음식'")

C_restaurant = Restaurant("'엔지니어 기사 식당'")
C_restaurant.open()
C_restaurant.restaurant("'파이썬 코딩'")