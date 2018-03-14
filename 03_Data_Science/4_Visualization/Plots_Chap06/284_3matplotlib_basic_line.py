### 6.1 matplotlib - 3 선 그래프
## 선 그래프는 수치의 변화를 선으로 이어 그린다 -> 시간에 따른 데이터 변화 추세를 보여준다.

from numpy.random import randn
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plot_data1 = randn(50).cumsum()     ## randn() 함수를 사용하여 임의의 데이터를 만든다. -> 랜덤으로 50개를 만든다.
plot_data2 = randn(50).cumsum()
plot_data3 = randn(50).cumsum()
plot_data4 = randn(50).cumsum()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

## 모양이 서로 다른 선 그래프 4개를 만든다.
ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')     ## label : 범례에 표시되는 레이블을 지정
ax1.plot(plot_data2, marker=r'^', color=u'red', linestyle='--', label='Red Dashed')
ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='Green Dash Dot')
ax1.plot(plot_data4, marker=r'1', color=u'orange', linestyle=':', label='Orange Dotted')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title('Line Plots: Marker, Colors, and Linestyles')
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend(loc='best')  ## 그래프의 범례를 만드는 코드 -> ※1 loc='best' : 그래프에서 최상의 위치에 자동적으로 범례가 배치
plt.savefig('line_plot.png', dpi=400, bbox_inches='tight')
plt.show()


### ※1 loc='' : 그래프 상의 범례 위치
## best, upper right, upper left, lower left, lower right, right, center left, center right, lower center, upper center, center