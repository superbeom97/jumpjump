def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return (fib(n-1)+fib(n-2)) # ((n-1)+(n-2))가 아니라, (n-1)과 (n-2)를 fib에 대입한 값들을 더해야 돼!

n = 10
print(fib(n))  # def 뒤에 있는 함수명과 입력인수를 print 해주는 거야!


def sum(a, b):
    result = a + b
    return result

a = 3
b = 4
print(sum(a,b)) # def 뒤에 있는 함수명과 입력인수를 print 해주는 거야!