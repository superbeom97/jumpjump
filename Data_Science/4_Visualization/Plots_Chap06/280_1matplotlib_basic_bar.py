## matplotlib 모듈 설치
## cmd 창에서 -> py -m pip install matplotlib

### 6.1 matplotlib - 1 막대 그래프
## matplotlib(맷플롯립)은 고품질의 그래프를 만들기 위한 목적의 패키지

import matplotlib.pyplot as plt
plt.style.use('ggplot')
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, rotation=0, fontsize='small')
plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()