### 6.1 matplotlib - 2 히스토그램
## 히스토그램은 수치형 데이터의 분포를 나타낸다.
## ↳ 빈도(도수), 빈도밀도(도수밀도), 확률, 확률밀도 등의 분포를 그릴 때 사용

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
mu1, mu2, sigma = 100, 130, 15  ## x1의 평균 = 100, x2의 평균 = 130 // sigma는 ??

## 난수 생성 함수를 사용하여 정규분포를 따르는 두 개의 변수 x1과 x2를 만든다.
x1 = mu1 + sigma*np.random.randn(10000)    ## randn() 함수의 범위 : -1 ~ +1 // 범위가 0~9,999가 아니라 10,000개의 데이터를 생성해 줌
x2 = mu2 + sigma*np.random.randn(10000)    ## ???

fig = plt.figure()  ## 그림을 만들고
ax1 = fig.add_subplot(1,1,1)    ## 하위 그래프를 추가 - 1,1,1 : ax1이 유일한(1행, 1열, 1개) 하위 그래프임을 의미

## 두 변수에 대한 히스토그램을 만든다.             ## ↱ bins=50은 수치를 50개의 구간(bin)으로 표시
n, bins, patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')   ## normed=False는 확률밀도가 아니라 빈도를 표시한다는 뜻
n, bins, patches = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)   ## alpha=0.5는 투명도로서 두 번째 히스토그램을 더 연하게 보이게 한다.

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')        ## X축 눈금 위치를 아래쪽, Y축 눈금 위치를 왼쪽으로 지정

plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histograms', fontsize=14, fontweight='bold')      ## fontsize : 글꼴 크기 // fontweight : 글꼴 - bold : 굵게
ax1.set_title('Two Frequency Distributions')    ## X축 레이블, Y축 레이블, 그래프 제목, 부제목 추가
plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
plt.show()