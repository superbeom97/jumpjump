class Unit: # 클래스의 상속 개념을 스타크래프트 테란을 예로 보면
    에너지  # 공통적인 것들을 super class에 다 적어주는
    방어력
    유닛타입
    이름
    x좌표
    y좌표

    def 정찰(self):
    def 이동(self):
    def 정지(self):


class SCV(Unit): # 공통적인 것을 제외한 scv만의 속성과 행위를 적어 주면 돼
    공격력
    사거리
    공격타입
    이름

    def 자원채취(self):
    def 공격(self):
    def 건물건설(self):
    def 수리(self):
