import requests

# 要提交的键值对的一个结构
keywords = {
    'file': 'img',
    'submit': '',
}

pictures = {
    'img': open("0.jpg", 'rb') # 这里的'img'键值对是form
}

# 表单要提交到的目的地址
url = "http://localhost:8080/CloudTensorFlow/YOLO_V3_dective/"

# 以post的方式提交表单并保存结果在变量r中
r = requests.post(url, data=keywords, files=pictures)
print(r.text)
