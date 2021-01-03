'''
TODO:
'''


'''
基础知识:
1. random.expovariate(miu) 生成均值为 1/miu 的指数分布的随机数 
2. 泊松过程的强度参数的意义：如果泊松过程的强度参数为 lambda，则在单位时间上新增一次的概率为 lambda，lambda 越大事件越可能发生
3. 泊松事件的事件间隔彼此独立且服从参数为 lambda 的指数分布
'''

'''
实现的细节:
1. 统计函数没有将仿真结束时没有被服务完的人算入
'''

import simpy
import random
from time import time
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

## 随机种子
randomSeed = time() # time()

## 指数分布的均值
miuService = 1  # 服务一个人的平均时间为 1 / 单位时间平均离开 1 个人
lambdaReachInterval = 0.5  # 单位时间平均来 0.5 个人

## 服务台的数目
numService = 1

## 仿真程序运行的时间
Until = 100

## 系统容量
systemCapacity = None # None 表示无容量限制 max(10,numService)

## 最大等待时间
maxWaiteTime = Until

## 初始队列长度
initLen = 1

## 客户类
class Customer(object):
    def __init__(self,index_,startTime_,queueLenStart_,reachInterval_):
        self.index = index_ # 第几个来到队列中来的
        self.startTime = startTime_ # 开始时间
        self.getServedTime = None # 开始被服务的时间
        self.endTime = None # 结束时间 
        self.queueLenStart = queueLenStart_ # 开始排队时队列长度
        self.queueLenEnd = None # 结束排队时队列长度
        self.reachInterval = reachInterval_  # 空闲了多长时间本 customer 才到达


## 顾客列表
customerList = []

## 当前队列长度
queueLen = 0


class System(object):
    def __init__(self, env, numService,miuService_):
        self.env = env
        self.service = simpy.Resource(env, numService)
        self.miuService =  miuService_

        
    def beingServed(self):
        # 服务事件为均值为 miuService 的指数分布
        yield self.env.timeout(random.expovariate(self.miuService))

def inoutQueue(env, moviegoer, sys):
    # 等待被服务 
    with sys.service.request() as request:  #观众向收银员请求购票
        yield request  | env.timeout(maxWaiteTime)  #观众等待收银员完成面的服务，超过最长等待事件maxCashierTime就会离开
        global customerList
        customerList[moviegoer].getServedTime = env.now
        yield env.process(sys.beingServed()) 
            
    # 完善统计资料
    global queueLen
    queueLen -= 1
    customerList[moviegoer].endTime = env.now
    customerList[moviegoer].queueLenEnd = queueLen


def runSys(env, numService,miuService):
    sys = System(env, numService, miuService)
    global initLen,customerList
    moviegoer = initLen
    for moviegoer in range(initLen):#初始化设置，开始的队伍长度为 initLen
        customerList.append(Customer(moviegoer,env.now,initLen,0))
        env.process(inoutQueue(env, moviegoer, sys))
    global queueLen
    queueLen = initLen 
    while True:
        reachInterval_ = random.expovariate(lambdaReachInterval)
        yield env.timeout(reachInterval_) # 顾客到达时间满足 lambdaReachInterval 的指数分布
        if systemCapacity == None or queueLen <= systemCapacity:  
            moviegoer += 1
            queueLen += 1
            customerList.append(Customer(moviegoer,env.now,queueLen,reachInterval_))
            env.process(inoutQueue(env, moviegoer, sys))

def plotSimRes(customerList):
    #! 初始设置
    # 用于正常显示中文标签
    plt.rcParams['font.sans-serif']=['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus']=False


    def plotTime_Service(customerList):
        plt.figure(figsize=(14,7)) # 新建一个画布
        plt.xlabel('时间/min')
        plt.ylabel('用户序列')
        servedUser = 0
        for customer in customerList:
            y = [customer.index]*2

            # 等待时间 
            if customer.endTime == None:
                customer.endTime = Until
                color = 'r'
            else:
                color = 'b'
                servedUser += 1
            x = [customer.startTime,customer.endTime]
            plt.plot(x,y,color=color)

            # 被服务的时间
            if customer.getServedTime != None and customer.endTime != Until:
                color = 'g'
                x = [customer.getServedTime,customer.endTime]
                plt.plot(x,y,color=color)

        plt.title("时间-队列-服务图 服务的用户数：%d" % servedUser)

    def plotQueueLen_time(customerList):
        plt.figure(figsize=(14,7)) # 新建一个画布
        plt.xlabel('时间/min')
        plt.ylabel('队列长度/人')
        

        queueLenList = []

        for customer in customerList:
            queueLenList.append([customer.startTime,customer.queueLenStart])
            queueLenList.append([customer.endTime,customer.queueLenEnd])
        queueLenList.sort()

        preTime = 0
        preLen = 0
        integralQueueLen = 0
        maxLen = 0
        global Until
        timeInCount = Until
        for each in queueLenList:
            if each[1] != None:
                x = [each[0]] * 2
                y = [0,each[1]]
                plt.plot(x,y,color='b')
                plt.plot(each[0],each[1],'bo')
            else:
                timeInCount = preTime
                break # 没有把仿真结束时未被服务完的人算进来
            integralQueueLen += (each[0] - preTime) * preLen
            preTime = each[0]
            preLen = each[1]
            maxLen = max(maxLen,each[1])
        
        averageQueueLen = integralQueueLen / timeInCount
        plt.title("时间-队列长度图 平均队列长度：%f" % averageQueueLen)
        
        
    def plotWaiteTime_time(customerList):
        plt.figure(figsize=(14,7)) # 新建一个画布
        plt.xlabel('时间/min')
        plt.ylabel('等待时间/min')
        

        queueLenList = []
        peopleInCount = 0
        for customer in customerList:
            if customer.getServedTime != None:
                peopleInCount += 1
                queueLenList.append([customer.startTime,customer.getServedTime - customer.startTime])
        queueLenList.sort()
        
        integralWaiteTime = 0
        maxWaiteTime = 0
        for each in queueLenList:
            x = [each[0]] * 2
            y = [0,each[1]]
            integralWaiteTime += each[1]
            maxWaiteTime = max(maxWaiteTime,each[1])
            plt.plot(x,y,color='b')
            plt.plot(each[0],each[1],'bo')

        averageWaiteTime = integralWaiteTime / peopleInCount
        
        plt.title("时间-等待时间图 平均等待时间：%f" % averageWaiteTime)

    def plotWaiteTime_time_QueueLen(customerList):
        fig = plt.figure(figsize=(14,7)) # 新建一个画布
        ax = fig.gca(projection='3d')
        plt.xlabel('时间/min')
        plt.ylabel('队列长度/人')
        ax.set_zlabel('等待时间/min')
        plt.title("时间-队列长度-等待时间图")

        queueLenList = [] # 格式：时间 队列长度 等待时间

        global Until
        for customer in customerList:
            if customer.getServedTime != None: # 没有把仿真结束时未被服务完的人算进来
                queueLenList.append([customer.startTime,customer.queueLenStart,customer.getServedTime-customer.startTime])
        queueLenList.sort(key=lambda x:x[0])

        for each in queueLenList:
            if each[1] != None:
                x = [each[0]]*2
                y = [each[1]]*2
                z = [0,each[2]]
                ax.plot(x,y,z,color='b')
                ax.scatter(x[1],y[1],z[1],c='b')

    plotTime_Service(customerList)
    plotQueueLen_time(customerList)
    plotWaiteTime_time(customerList)
    # plotWaiteTime_time_QueueLen(customerList)
    plt.show()



def main():
    random.seed(randomSeed)
    #运行模拟场景
    env = simpy.Environment()
    env.process(runSys(env, numService,miuService))
    env.run(until=Until) # 仿真时长，并不保证所有的事件都结束了
    
    #查看统计结果
    plotSimRes(customerList)

main()

