class Calculator:
    def __init__(self, number):
        self.one = number[0]
        self.two = number[1]
        self.three = number[2]
        self.four = number[3]
        self.five = number[4]

    def sum(self):
        sum_result = self.one + self.two + self.three + self.four + self.five
        print(sum_result)

    def avg(self):
        avg_result = (self.one + self.two + self.three + self.four + self.five) / 5
        print(avg_result)

cal1 = Calculator([1,2,3,4,5])
cal2 = Calculator([6,7,8,9,10])

if __name__ == "__main__":
    cal1.sum()
    cal1.avg()
    cal2.sum()
    cal2.avg()