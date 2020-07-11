from PIL import Image
import math
import pygame
# 导入pygame库
from pygame.locals import *
# 导入一些常用的函数和常量
from sys import exit
# 向sys模块借一个exit函数用来退出程序
from sys import argv


info = ['c 测量两点的距离', 'l 测量一段折线的长度', 'j 经纬度推算', '测量经纬度时的比例尺是347.1',
        'raw.png 家族比例尺 = 0.1721', '集装箱位置.png 家族比例尺 = 0.3025']
for each in info:
    print(each)


def main(argvs):
    background_image_filename = argvs[1]
    img = Image.open(background_image_filename)
    m, n = img.size
    # 指定图像文件名称
    pygame.init()
    # 初始化pygame,为使用硬件做准备

    screen = pygame.display.set_mode((m, n), 0, 32)
    # 创建了一个窗口
    pygame.display.set_caption("Get RGB from Mouse Location")
    # 设置窗口标题

    background = pygame.image.load(background_image_filename).convert()
    # 加载并转换图像

    while True:
        # 游戏主循环

        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后退出程序
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                pixel_rgb = img.getpixel((x, y))
                print(pixel_rgb, x, y)
        keys = pygame.key.get_pressed()
        if keys[K_c]:
            print('进入测量模式')
            bilichi = input('请输入比例尺')
            bilichi = float(bilichi)
            flag = 1
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        # 接收到退出事件后退出程序
                        exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if flag == 1:
                            x0, y0 = pygame.mouse.get_pos()
                            flag += 1
                        else:
                            x1, y1 = pygame.mouse.get_pos()
                            if x1 < 50 and y1 < 50:
                                print('请重新选择起始点')
                                flag = 1
                                continue
                            dist = bilichi * \
                                math.sqrt((x1 - x0) * (x1 - x0) +
                                          (y1 - y0) * (y1 - y0))
                            print('距离为%f' % dist)

        if keys[K_l]:
            print('进入测距模式')
            bilichi = input('请输入比例尺')
            bilichi = float(bilichi)
            D = 0

            while True:

                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        '''
                            print(x,y)
                            x,y = pygame.mouse.get_pos()
                            print(x,y)
                            '''
                        if x < 50 and y < 50:
                            flag = 1
                            print('请选定起点')
                            continue
                        if x > (m - 50) and y < 50:
                            print('距离是', D)
                            flag = -1
                            D = 0
                            continue
                        if flag == 1:

                            x0, y0 = x, y
                            flag = 2
                        elif flag == 2:
                            x1, y1 = x, y
                            D += bilichi * \
                                math.sqrt((x1 - x0) * (x1 - x0) +
                                          (y1 - y0) * (y1 - y0))
                            x0, y0 = x1, y1

        if keys[K_j]:
            print('进入精度纬度推算模式')
            bilichi = input('请输入比例尺')  # 347.1像素每度
            bilichi = float(bilichi)
            print('请点击已知经纬度的位置')
            flag = 1
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        # 接收到退出事件后退出程序
                        exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if flag == 1:
                            x0, y0 = pygame.mouse.get_pos()
                            flag += 1
                            temp_str = input('请输入选取点的经纬度坐标。格式 经度 纬度\n')
                            temp_str = temp_str.split(' ')
                            jingdu = temp_str[0]
                            weidu = temp_str[1]
                            jingdu = float(jingdu)
                            weidu = float(weidu)
                        else:
                            x1, y1 = pygame.mouse.get_pos()
                            temp_jingdu = jingdu + (x1 - x0) / bilichi
                            temp_weidu = weidu - (y1 - y0) / bilichi
                            print('经度 ', temp_jingdu, ' 纬度 ', temp_weidu)

        screen.blit(background, (0, 0))
        # 将背景图画上去

        pygame.display.update()
        # 刷新一下画面


if __name__ == '__main__':
    main(argv)
