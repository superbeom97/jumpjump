a = [1, 2, 5, 7, 9, 3, 4]
print(a[0])
print(a[1])
a[0] = a[1]
a[1] = a[0]
print("")
print(a[0])
print(a[1])

a.sort()
print(a)