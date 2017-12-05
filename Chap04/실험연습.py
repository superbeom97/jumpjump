import sys

greet_users = sys.argv[1:]
for i in greet_users:
    print("Hello, ", end="")
    print(i[0].upper() + i[1:] + '!')