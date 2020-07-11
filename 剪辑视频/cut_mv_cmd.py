from moviepy.video.io.VideoFileClip import VideoFileClip
import sys
from functools import reduce


def to_seconds(x, y):
    return 60 * x + y


def main(source):
    print('要剪切的视频是', source[1])  # 获取需要剪切的文件
    source = source[1]
    time = input('请输入开始和结束的时间:\n')  # 获取开始剪切时间
    time = time.split()
    times = []
    while time != []:

        start_time = time.pop(0)
        stop_time = time.pop(0)
        times.append([start_time, stop_time])

    print("子视频命名方式为原名称_段数.mp4")
    temp = source.split('.')
    target = []
    num_of_cuts = len(times)
    for i in list(range(1, num_of_cuts + 1)):
        target.append(temp[0] + str(i) + '.' + temp[1])

    # print('**--**',target)
    video = VideoFileClip(source)
    for i in list(range(0, num_of_cuts, 1)):
        current_time = times[i]
        print('cutting...\n')

        temp = list(map(int, current_time[0].split(":")))
        start_time = reduce(to_seconds, temp)
        temp = list(map(int, current_time[1].split(":")))
        stop_time = reduce(to_seconds, temp)
        new_video = video.subclip(start_time, stop_time)  # 执行剪切操作
        new_video.to_videofile(target[i], fps=29, remove_temp=True)  # 输出文件

    video.close()
    print('done ^_^\n')


if __name__ == "__main__":
    main(sys.argv)
