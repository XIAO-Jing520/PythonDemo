import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt

'''
基础知识
1. pdf 概率密度函数
2. pmf 离散型随机变量分布律
3. cdf 分布函数
4. ppf 百分位函数（累计分布函数的逆函数）
5. lsf 生存函数的逆函数（1 - cdf 的逆函数）
'''
#! 初始设置
# 用于正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus']=False


#! 正态分布
points = 100

loc = 10 # loc 均值 scale 方差
scale = 10

x1 = np.linspace(st.norm.ppf(0.0001, loc=loc, scale=scale),st.norm.ppf(0.9999, loc=loc, scale=scale), points) # ppf 是 cdf 的逆函数
y1 = st.norm.pdf(x1, loc=loc, scale=scale) # 概率密度
y2 = st.norm.cdf(x1, loc=loc, scale=scale) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.show()
