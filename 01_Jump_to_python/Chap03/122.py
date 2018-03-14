treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


# 디버깅 하는 방법
# 마우스로 탭 번호 칸(4번 칸)을 눌러 >> 그럼 빨간 원이 생긴다 >> Shift+F9
# >> Watches 창 아이콘 눌러서 # Wahtes 창 열기 >> +안경 아이콘 눌러서 treeHit<10 입력
# >> F8(번 누르면 한 번씩 실행)번 눌러서 실행 과정 살펴보기
# >> 그리고 잘못된 부분 수정하기