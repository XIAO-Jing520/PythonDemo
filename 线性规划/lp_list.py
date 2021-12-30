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
sw = []
sw.append(LpVariable("sw1", cat=LpBinary))
sw.append(LpVariable("sw2", cat=LpBinary))
sw.append(LpVariable("sw3", cat=LpBinary))
sw.append(LpVariable("sw4", cat=LpBinary))
sw.append(LpVariable("sw5", cat=LpBinary))

fsw = []
fsw.append([1,0,1])
fsw.append([0,0,1])
fsw.append([0,0,1])
fsw.append([1,1,0])
fsw.append([0,0,0])

## 优化目标
sc_mrf += z

## 约束1：集合覆盖
for i in range(0,len(fsw[0])):
    tmp = fsw[0][i]*sw[0]
    for j in range(1,len(sw)):
        tmp += fsw[j][i]*sw[j]
    sc_mrf += tmp >= 1


## 本质上是优化目标，但是转换为了约束2：最小重复流上报
for i in range(0,len(fsw[0])):
    tmp = fsw[0][i]*sw[0]
    for j in range(1,len(sw)):
        tmp += fsw[j][i]*sw[j]
    sc_mrf += z >= tmp

sc_mrf.solve()

print("Status:", LpStatus[sc_mrf.status])

for v in sc_mrf.variables():
    print(v.name, "=", v.varValue)

    solution.append(v.varValue)

print("objective=", value(sc_mrf.objective))

