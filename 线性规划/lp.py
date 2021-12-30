# 参考： http://fancyerii.github.io/2020/04/18/pulp/
# 文档： https://coin-or.github.io/pulp/ https://coin-or.github.io/pulp/plugins/lparray.html

from pulp import *


sc_mrf = LpProblem("SetCover-MinRepeatFlow", LpMinimize)

"""
flowID  |    sw ID
        |_______________
        |  1  2  3  4  5
________|_______________
   1    |  1  0  0  1  0
   2    |  0  0  0  1  0
   3    |  1  1  1  0  0

"""

solution = []

z = LpVariable("z", lowBound=0, cat=LpInteger)
sw1 = LpVariable("sw1", cat=LpBinary)
sw2 = LpVariable("sw2", cat=LpBinary)
sw3 = LpVariable("sw3", cat=LpBinary)
sw4 = LpVariable("sw4", cat=LpBinary)
sw5 = LpVariable("sw5", cat=LpBinary)

fsw1 = [1,0,1]
fsw2 = [0,0,1]
fsw3 = [0,0,1]
fsw4 = [1,1,0]
fsw5 = [0,0,0]


## 优化目标
sc_mrf += z

## 约束1：集合覆盖
for i in range(0,len(fsw1)):
    sc_mrf += fsw1[i]*sw1 + fsw2[i]*sw2 + fsw3[i]*sw3 + fsw4[i]*sw4 + fsw5[i]*sw5 >= 1


## 本质上是优化目标，但是转换为了约束2：最小重复流上报
for i in range(0,len(fsw1)):
    sc_mrf += z >= fsw1[i]*sw1 + fsw2[i]*sw2 + fsw3[i]*sw3 + fsw4[i]*sw4 + fsw5[i]*sw5


sc_mrf.solve()

print("Status:", LpStatus[sc_mrf.status])

for v in sc_mrf.variables():
    print(v.name, "=", v.varValue)

    solution.append(v.varValue)

print("objective=", value(sc_mrf.objective))

