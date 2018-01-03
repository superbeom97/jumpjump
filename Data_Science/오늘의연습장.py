class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        print(self.result)

cal1 = Calculator()
cal1.adder(5)
cal1.adder(7)

#