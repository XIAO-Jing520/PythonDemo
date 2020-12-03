from moviepy.editor import *

videoName = input('视频路径：（请勿输入空白视频）\n')
video = VideoFileClip(videoName)  
audio = video.audio
audio.write_audiofile('audio.mp3') 
