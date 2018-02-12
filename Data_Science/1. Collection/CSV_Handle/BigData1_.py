# import os           ## 현재 디렉터리 위치를 반환해 주는, 이 디렉터리에
# print(os.getcwdb()) ## Demographic_Statistics_By_Zip_Code.csv 파일이 있어야 해!!


import csv          ## 데이터를 불러오는 소스 코드

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:  ## 데이터를 불러오는 소스 코드
    data = list(csv.reader(infile))

## No1_COUNT PARTICIPANTS
countParticipantsIndex = data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS': %s" % countParticipantsIndex)
# print("The index of 'COUNT PARTICIPANTS': " +str(countParticipantsIndex))

countParticipants = []
# index = 0

for row in data[1:]:
    countParticipants.append(int(row[countParticipantsIndex]))

print("The contents of 'COUNT PARTICIPANTS': %s" % countParticipants)


## No2_COUNT CITIZEN STATUS TOTAL
countCitizenStatusTotalIndex = data[0].index("COUNT CITIZEN STATUS TOTAL")
print("The index of 'COUNT CITIZEN STATUS TOTAL': %s" % countCitizenStatusTotalIndex)

countCitizenStatusTotal = []

for row in data[1:]:
    countCitizenStatusTotal.append(int(row[countCitizenStatusTotalIndex]))

print("The contents of 'COUNT CITIZEN STATUS TOTAL': %s" % countCitizenStatusTotal)


## No3_COUNT FEMALE
countFemaleIndex = data[0].index("COUNT FEMALE")
print("The index of 'COUNT FEMALE': %s" % countFemaleIndex)

countFemale = []

for row in data[1:]:
    countFemale.append(int(row[countFemaleIndex]))

for i in countFemale:       ## 하나하나 풀어서 출력
    print(i)

# print("The contents of 'COUNT FEMALE': %s" % countFemale)