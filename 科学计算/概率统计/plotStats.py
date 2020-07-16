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


官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html
'''
#! 初始设置
# 用于正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus']=False

#! 伯努利分布/两点分布/0-1分布
points = 100

p = 0.5

x1 = np.arange(st.bernoulli.ppf(0.01, p),
            st.bernoulli.ppf(0.99,p)+1) # 0-1 分布只有两个值

x2 = np.linspace(0,1, points) # 除了 0 和 1 之外的所有点的 P 均为 0，但是还是加上这些 P=0 的点为了让分布图看起来更符合实际情况
y1 = st.bernoulli.pmf(x1,p) # 概率密度，当 x 取 0 或者 1 时，函数返回值为 p 或 1-p，其余 x 的取值返回 0
y2 = st.bernoulli.cdf(x2,p) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("伯努利分布/两点分布/0-1分布 p=%f" % (p))
plt.plot(x1,y1,'o',label="概率分布")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x2,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方



#! 二项分布
points = 1000

n= 20
p = 0.5

x1 = np.arange(st.binom.ppf(0.01, n, p),
            st.binom.ppf(0.99, n, p)+1) # 使用 arange 保证 x1 的值是可行值  
x2 = np.linspace(st.binom.ppf(0.01, n, p),
            st.binom.ppf(0.99, n, p),
            points) # 使用 linspace 使分布函数的曲线更加平滑
y1 = st.binom.pmf(x1,n,p) # 概率密度
y2 = st.binom.cdf(x2,n,p) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("二项分布 n=%f,p=%f" % (n,p))
plt.plot(x1,y1,'o',label="概率分布")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x2,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方




#! 泊松分布
points = 1000

Lambda = 5

x1 = np.arange(st.poisson.ppf(0.0001, Lambda),
              st.poisson.ppf(0.9999, Lambda)+1) # 使用 arange 保证 x1 的值是可行值  
x2 = np.linspace(st.poisson.ppf(0.01, Lambda),
              st.poisson.ppf(0.99, Lambda),
            points) # 使用 linspace 使分布函数的曲线更加平滑
y1 = st.poisson.pmf(x1,Lambda) # 概率密度，泊松分布的概率密度的横轴表示在单位时间内发生“事故”次数的概率，纵轴是发生这种“事故”次数的概率
# 比如说： x=0,p=0.1 表示在作为研究对象的时间段内，发生 0 此事故的概率是 0.1；x=5,p=0.4 表示在作为研究对象的时间段内，发生 5 此事故的概率是 0.4
y2 = st.poisson.cdf(x2,Lambda) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("泊松分布 Lambda=%f" % (Lambda))
plt.plot(x1,y1,'o',label="概率分布")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x2,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方





#! 均匀分布

points = 100

loc = 5 # 相当于 a 
scale = 10 # 相当于 b-a

x1 = np.linspace(st.uniform.ppf(0.01,loc=loc,scale=scale),
                st.uniform.ppf(0.99,loc=loc,scale=scale), 
                points) # 连续性随机变量就没必要分 x1 x2 了
y1 = st.uniform.pdf(x1, loc=loc, scale=scale) # 概率密度
y2 = st.uniform.cdf(x1, loc=loc, scale=scale) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("均匀分布 a=%f,b=%f" % (loc,loc+scale))
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方




#! 指数分布

points = 100

loc = 0 # x 的偏移
scale = 10 # 相当于 1/Lambda

x1 = np.linspace(st.expon.ppf(0.01,loc=loc,scale=scale),
                st.expon.ppf(0.99,loc=loc,scale=scale), 
                points) # 连续性随机变量就没必要分 x1 x2 了
y1 = st.expon.pdf(x1, loc=loc, scale=scale) # 概率密度
y2 = st.expon.cdf(x1, loc=loc, scale=scale) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("指数分布 Lambda=%f" % (1/scale))
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方




#! 正态分布

points = 100

loc = 10 # loc 均值 scale 方差
scale = 10

x1 = np.linspace(st.norm.ppf(0.0001, loc=loc, scale=scale),
                    st.norm.ppf(0.9999, loc=loc, scale=scale), 
                        points) # ppf 是 cdf 的逆函数
y1 = st.norm.pdf(x1, loc=loc, scale=scale) # 概率密度
y2 = st.norm.cdf(x1, loc=loc, scale=scale) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("正态分布 loc=%f,scale=%f" % (loc,scale))
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方



# 伽马分布
## 我自己的实现
from functools import partial  # 绑定参数
from scipy import integrate # 求定积分


## 官方的实现
alpha = 5
beta = 5


c = beta
a = alpha/c

x1 = np.linspace(st.gengamma.ppf(0.0001, a,c),
                st.gengamma.ppf(0.9999, a,c), points)



y1 = st.gengamma.pdf(x1, a,c)

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("伽马分布 alpha=%f,beta=%f" % (alpha,beta))
plt.subplot(121)
plt.plot(x1, y1)


y2 = st.gengamma.cdf(x1, a,c)
plt.subplot(122)
plt.plot(x1, y2)


#! 对数正态分布

points = 100

loc = 0 # loc 均值 scale 方差
scale = 1
s = 0.1 # 相当于 omiga


x1 = np.linspace(st.lognorm.ppf(0.0001, s = s,loc=loc, scale=scale),
                    st.lognorm.ppf(0.9999, s = s,loc=loc, scale=scale), 
                        points) # ppf 是 cdf 的逆函数
y1 = st.lognorm.pdf(x1, s = s,loc=loc, scale=scale) # 概率密度
y2 = st.lognorm.cdf(x1, s = s,loc=loc, scale=scale) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("对数正态分布 loc=%f,scale=%f,s=%f" % (loc,scale,s))
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方


#! 卡方分布

points = 100

df = 2 # 自由度


x1 = np.linspace(st.chi2.ppf(0.0001, df),
                    st.chi2.ppf(0.9999,df), 
                        points) # ppf 是 cdf 的逆函数
y1 = st.chi2.pdf(x1,df) # 概率密度
y2 = st.chi2.cdf(x1, df) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("卡方分布 df=%f" % (df))
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方


#! t 分布

points = 100

df = 10 # 自由度


x1 = np.linspace(st.t.ppf(0.0001, df),
                    st.t.ppf(0.9999,df), 
                        points) # ppf 是 cdf 的逆函数
y1 = st.t.pdf(x1,df) # 概率密度
y2 = st.t.cdf(x1, df) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("t分布 df=%f" % (df))
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方



#! F 分布

points = 100

dfn = 10
dfd = 12


x1 = np.linspace(st.f.ppf(0.0001,  dfn, dfd),
                    st.f.ppf(0.9999, dfn, dfd), 
                        points) # ppf 是 cdf 的逆函数
y1 = st.f.pdf(x1, dfn, dfd) # 概率密度
y2 = st.f.cdf(x1,  dfn, dfd) # 分布函数

plt.figure(figsize=(14,7)) # 新建一个画布
plt.subplot(121)
plt.title("f分布 dfn=%f,dfd=%f" % (dfn,dfd))
plt.plot(x1,y1,label="概率密度函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方

plt.subplot(122)
plt.plot(x1,y2,label="分布函数")
plt.legend(loc='upper left') #loc指定小图标的位置,upper上方，lower下方





plt.show() # 最后的时候一次性绘制所有的 figure
