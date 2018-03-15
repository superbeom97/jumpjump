### 7.2 와인 품질 데이터셋 - 2 그룹화, 히스토그램, t 검정
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

## 1 기술 통계
# 데이터셋을 팬더스 데이터프레임으로 읽기
wine = pd.read_csv('Housing.csv', sep=',', header=0)
for z in wine:
    if z == 'yes':
        z = 1
    elif z == 'no':
        z = 0
wine = wine.replace('yes', '1')
print(wine)
# print(wine.head())


# ## 2 그룹화, 히스토그램, t 검정
# # 와인 종류에 따른 기술 통계를 출력하기
# # print(wine.groupby('type')[['quality']].describe().unstack('type'))
#
# # 특정 사분위수 계산하기
# # print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
#
# # # 와인 종류에 따른 품질의 분포 확인하기
# # red_wine = wine.ix[wine['type']=='red', 'quality']
# # white_wine = wine.ix[wine['type']=='white', 'quality']
# #
# # sns.set_style("dark")
# # # print(sns.distplot(red_wine, norm_hist=True, kde=False, color="red", label="Red wine"))
# # # print(sns.distplot(red_wine, norm_hist=True, kde=False, color="red", label="Red wine"))
# # plt.utils.axlabel("Quality Score", "Density")
# # plt.title("Distribution of Quality by Wine Type")
# # plt.legend()
# # plt.show()
# #
# # # 와인 종류에 따라 품질의 차이 검정
# # print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
# # tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
# # print('tstat: %.3f  pvalue: %.4f' % (tstat, pvalue))
#
#
# # ## 3 상관 관계 분석
# # # 모든 변수 쌍 사이의 상관계수 구하기
# # print(wine.corr())      ## corr() :  모든 변수 쌍 사이의 상관계수를 구한다.
# #
# # 변수 간 관계 살펴보기
# def take_sample(data_frame, replace=False, n=200):
#     return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
#
# reds_sample = take_sample(wine.loc[wine['type']=='red', :])
# whites_sample = take_sample(wine.loc[wine['type']=='white', :])
# wine_sample = pd.concat([reds_sample, whites_sample])
# wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
#
# print(pd.crosstab(wine.in_sample, wine.type, margins=True))
#
# sns.set_style("dark")
#
# g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci":False, "x_jitter":0.25, "y_jitter":0.25},
#                  hue='type', diag_kind='hist', diag_kws={"bins":10, "alpha":1.0}, palette=dict(red="red", white="white"),
#                  markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
# # print(g)
#
# plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14,
#              horizontalalignment='center', verticalalignment='top', x=0.5, y=0.999)
# # plt.show()
#
#
# ## 4 최소제곱법을 이용한 선형회귀분석
# my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + density + fixed_acidity + free_sulfur_dioxide + pH +' \
#              'residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
#
#
# lm = ols(my_formula, data=wine).fit()
# # 또는 lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
#
# print(lm.summary())
# print("\nQuantities you can extract from the result:\n%s" % dir(lm))
# print("\nCoefficients:\n%s" % lm.params)
# print("\nCoefficient Std Errors:\n%s" % lm.bse)
# print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
# print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
# print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))
#
#
# ## 6 독립변수의 표준화
# # 와인 데이터셋의 quality를 종속변수로 생성
# dependent_variable = wine['quality']
# independet_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
# independet_variables_standardized = (independet_variables - independet_variables.mean()) / independet_variables.std()
# wine_standardized = pd.concat([dependent_variable, independet_variables_standardized], axis=1)
#
# lm_standardized = ols(my_formula, data=wine_standardized).fit()
# print(lm_standardized.summary())
#
#
# ## 7 예측하기
# # 기존 데이터셋의 첫 10개 값을 가지고 '새로운' 관측값 데이터셋을 만듦
# new_observations = wine.ix[wine.index.isin(range(10)), independet_variables.columns]
# y_predicted = lm.predict(new_observations)
# y_predicted_rounded = [round(score, 2) for score in y_predicted]
# print(y_predicted_rounded)