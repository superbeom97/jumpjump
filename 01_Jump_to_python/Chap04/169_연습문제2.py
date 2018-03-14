f = open("sample.txt")
lines = f.read()
print(lines)
f.close()

total = 0
for line in lines:
    score = line
    total += int(score)
    print(total)


#average = total / len(line)
#print(average)

#f = open("result.txt", 'w')
#f.write(average)
#f.close()