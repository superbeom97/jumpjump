i=0
while True:
    i+=1
    if i>5: break
    print("*"*i)


a=[70,60,55,75,95,90,80,80,85,100]
total=0
for total in a:
    total+=range(len(a))
average=total%len(a)
print(average)


a=[70,60,55,75,95,90,80,80,85,100]
sum=0
for i in a:
    sum=sum+i
print(sum)