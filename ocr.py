
import cv2
import pytesseract
from pytesseract import Output
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
 
def recoText(im):
    """
    识别字符并返回所识别的字符及它们的坐标
    :param im: 需要识别的图片
    :return data: 字符及它们在图片的位置
    """
    data = {}
    d = pytesseract.image_to_data(im, output_type=Output.DICT, lang='chi_sim')
    for i in range(len(d['text'])):
        if 0 < len(d['text'][i]):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            data[d['text'][i]] = ([d['left'][i], d['top'][i], d['width'][i], d['height'][i]])
 
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 1)
            # 使用cv2.putText不能显示中文，需要使用下面的代码代替
            #cv2.putText(im, d['text'][i], (x, y-8), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)
 
            pilimg = Image.fromarray(im)
            draw = ImageDraw.Draw(pilimg)
            # 参数1：字体文件路径，参数2：字体大小
            font = ImageFont.truetype("simhei.ttf", 15, encoding="utf-8")
            # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
            draw.text((x, y-10), d['text'][i], (255, 0, 0), font=font)
            im = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
 
    cv2.imshow("recoText", im)
    return data
 
if __name__ == '__main__':
    img = cv2.imread('2.png')
    #cv2.imshow("src", img)
    data = recoText(img)
 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
