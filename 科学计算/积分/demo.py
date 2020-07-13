import numpy as np
import matplotlib.pyplot as plt	#画图用
import scipy.integrate as si	#numpy求定积分用

#声明曲线函数
def f(x):
    return 2 * x ** 2 + 3 * 4 + 4



#1. 在区间[-5,5]间拆出1000个满足f(x)的点,画出该函数曲线
a, b = -5, 5
x1 = np.linspace(a, b, 1001)
y1 = f(x1)


area = si.quad(f,a,b)
print(area)

plt.plot(x1,y1)
plt.show()
