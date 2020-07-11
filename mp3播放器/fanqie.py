#encoding = utf-8
import os
from time import sleep, ctime


i = 1
while True:
    doit = input('开始？ y/n\n')
    if doit == 'y':

        print('第%d个番茄钟开始' % i)

        sleep(1*60*25)
        print('第%d个番茄钟结束，恭喜你' % i)
        print("当前时间 %s" % ctime())
        if i % 4 == 0:
            os.system('【】425.mp3')
            print('休息15~25min吧')
        else:
            os.system('25.mp3')
            print('休息3~5min吧')
        i += 1
        print(i)
