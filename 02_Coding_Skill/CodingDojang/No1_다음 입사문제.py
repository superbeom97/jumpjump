# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
#
# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.


S = [1, 3, 4, 8, 13, 17, 20, 21, 101, 102]
initial_value = 10000
for i in range(len(S)-1):
    sub_value = int(S[-(i+1)]) - int(S[-(i+2)])
    if sub_value < initial_value:
        initial_value = sub_value
    else:
        continue


for i in range(len(S)-1):
    if int(S[-(i+1)]) - int(S[-(i+2)]) == initial_value:
        print("(%s, %s)" % (S[-(i+2)], S[-(i+1)]))

    else:
        continue