## 문제가 명확하진 않지만....
# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?
#
# 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.
#
# 00:00 (60초간 표시됨)
# 00:01
# 00:02
# ...
# 23:59

def time():
    hour = 0
    minute = 0

    for i in range(24):
        if str(3) in str(i):
            hour += 60*60
        else:
            for j in range(60):
                if str(3) in str(j):
                    minute += 60

    return (hour + minute)

print(time())