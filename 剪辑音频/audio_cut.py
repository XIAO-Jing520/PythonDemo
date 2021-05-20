from pydub import AudioSegment
import sys
file = sys.argv[1]
start_time = int(sys.argv[2])
end_time = int(sys.argv[3])
print(file)

# 1秒=1000毫秒
SECOND = 1000
# 导入音乐
song = AudioSegment.from_mp3(file)

# 取 start_time 秒到 end_time 秒间的片段
song = song[start_time*SECOND:end_time*SECOND]

song.export('new'+file) 
