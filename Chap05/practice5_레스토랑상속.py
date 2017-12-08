class Restaurant:
    firstname = "대한민국 남바완"
    re_cuisine = '한식'
    re_time = "pm.7 ~"
    re_close = "매달 마지막"

    def __init__(self, name):
        self.fullname = self.firstname + " " + name

    def cuisine_restaurant(self, cuisine):
        self.fullcuisine = self.re_cuisine + " " + cuisine
        print("저희 레스토랑 %s은 %s 전문점입니다." % (self.fullname, self.fullcuisine))

    def time_restaurant(self, time):
        self.fulltime = self.re_time + " " + time
        print("저희 레스토랑 %s의 영업 시간은 %s입니다." % (self.fullname, self.fulltime))

    def close_restaurant(self, close):
        self.fullclose = self.re_close + " " + close
        print("저희 레스토랑 %s의 휴무일은 %s입니다." % (self.fullname, self.fullclose))

korea = Restaurant("본점")
korea.cuisine_restaurant("총괄")
korea.time_restaurant("am.1")
korea.close_restaurant("일요일")


class Daegu_Restaurant(Restaurant):
    re_close = "매달 첫 번째"

    def time_restaurant(self, time):
        self.fulltime = self.re_time + " " + time
        print("저희 레스토랑 %s의 영업 시간은 %s입니다." % (self.fullname, self.fulltime))

daegu = Daegu_Restaurant("대구점")
daegu.cuisine_restaurant("동인동 찜갈비")
daegu.time_restaurant("am2")
daegu.close_restaurant("토요일")


class Busan_Restaurant(Restaurant):