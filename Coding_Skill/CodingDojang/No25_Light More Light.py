# Light More Light
#
# 우리 학교에는 복도 불을 켜고 끄는 마부(Mabu)라는 사람이 있다. 전구마다 불을 켜고 끄는 스위치가 있다.
# 불이 꺼져 있을 때 스위치를 누르면 불이 켜지고 다시 스위치를 누르면 불이 꺼진다.
# 처음에는 모든 전구가 꺼져 있다. 마부라는 사람은 특이한 행동을 한다.
# 복도에 n개의 전구가 있으면, 복도를 n번 왕복한다.
# i번째 갈 때 그는 i로 나누어 떨어지는 위치에 있는 스위치만 누른다.
# 처음 위치로 돌아올 때는 아무 스위치도 건드리지 않는다.
# i번째 왕복은 (이런 이상한 행동을 하면서) 복도를 한 번 갔다가 오는 것으로 정의된다.
# 마지막 전구의 최종 상태를 알아내자. 과연 그 전구는 켜져 있을까 아니면 꺼져 있을까?
#
# <<Input>>
# 복도에 있는 n번째 전구를 나타내는 숫자가 입력된다. (2^32-1 이하의 정수가 입력된다.)
# 0은 입력의 끝을 의미하며 그 값은 처리하지 않는다.
#
# <<Output>>
# 그 전구가 켜져 있으면 "yes"를, 꺼져 있으면 "no"를 출력한다.
# 테스트 케이스마다 한 줄에 하나씩 출력한다.
#
# <<Sample Input>>
# 3
# 6241
# 8191
# 0
#
# <<Sample Output>>
# no
# yes
# no



# 처음에 모든 전구는 꺼져 있다
#
# n을 입력
#
# 3개의 전구, 3번 왕복
# 전구 = 1 2 3
# 처음에는 = off off off
# 첫 번째 갈 때 = on on on
# 두 번째 갈 때 = on off on
# 세 번째 갈 때 = on off off
#
# n 번째 전구가 켜져 있나? 꺼져 있나?

## 마지막 전구만 알아보면 돼 -> n의 약수일 때마다 스위치를 눌러
## => n의 약수를 구해야 돼
## 나눴을 때, 나머지가 0이면 약수!!

print("알아보고 싶은 전구와 왕복 횟수인 N을 입력하세요.")
print("(입력을 다 하셨으면 '0'을 입력해 주세요.) : ")
final_light = []
while True:
    count = 0
    n = int(input())
    if n != 0:
        for i in range(1, n+1):  # 마지막(n번째) 전구만 알아보면 돼 -> n의 약수를 구하는 식
            if n % i == 0:
                count += 1  # 약수의 개수를 카운트
            else:
                continue

        if count % 2 == 0:  # 약수의 개수가 짝수 이면 "OFF"
            final_light.append("OFF")
        else:               # 약수의 개수가 홀수이면 "ON"
            final_light.append("ON")
    else:
        for i in final_light:
            print(i)
        break