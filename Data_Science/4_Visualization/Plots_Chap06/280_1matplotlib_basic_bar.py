## matplotlib 모듈 설치
## cmd 창에서 -> py -m pip install matplotlib

### 6.1 matplotlib - 1 막대 그래프
## matplotlib(맷플롯립)은 고품질의 그래프를 만들기 위한 목적의 패키지
## ↳ 막대 그래프, 상자그림, 선 그래프, 산점도, 히스토그램 등 기본적인 통계 그래프를 만들 수 있고
##   데이터를 지도에 매핑하는 basemap 및 cartopy, 그리고 3D 그래프를 만드는 mplot3d 같은 도구도 제공한다.
## ↳ 모양과 크기, 축의 범위와 단위, 눈금과 레이블, 범례 및 제목 등을 직접 지정할 수 있다.

## 막대 그래프는 범주형 데이터의 수치를 요약한다.
## ↳ 가로, 세로, 누적, 그룹화된 막대 그래프를 사용한다.

import matplotlib.pyplot as plt

plt.style.use('ggplot')     ## ggplot 스타일시트를 사용하여 R용 시각화 패키지 ggplot2의 스타일을 재현한다.

## 그래프에 사용할 데이터를 만든다.
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']     ## customers 레이블
customers_index = range(len(customers))             ## customers_index 인덱스
sale_amounts = [127, 90, 201, 111, 232]

## matplotlib에서 그래프를 만들려면, 먼저 하나의 그림(figure)을 만들고 그 안에 하위 그래프(subplot)를 추가해야 한다.
fig = plt.figure()  ## 그림을 만들고
ax1 = fig.add_subplot(1,1,1)    ## 하위 그래프를 추가 - 1,1,1 : ax1이 유일한(1행, 1열, 1개) 하위 그래프임을 의미

ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')    ## 막대 그래프를 만든다.
ax1.xaxis.set_ticks_position('bottom')          ## ↳ X축은 customers_index // Y축은 sale_amounts // 막대가 X축 레이블의 중앙에 위치하도록 지정
ax1.yaxis.set_ticks_position('left')    ## X축 눈금 위치를 아래쪽, Y축 눈금 위치를 왼쪽으로 지정
plt.xticks(customers_index, customers, rotation=0, fontsize='small')    ## xtictks 함수에 인덱스와 레이블이 모두 필요 -> 위에서 선언해 놓음(customers, customers_index)

plt.xlabel('Customer Name')                 ## ↳ 막대의 눈금 레이블을 인덱스에서 실제 이름으로 변경, rotation=0은 눈금 레이블을 수평으로 지정
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')   ## X축 레이블, Y축 레이블, 그래프 제목 추가

plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')   ## bar_plot.png라는 파일명으로 저장, dpi=400 : 그림의 해상도 지정
plt.show()  ## 지금까지 만든 그림을 새 창에 출력            ## bbox_inches='tight' : 그림을 둘러싼 여백을 제거