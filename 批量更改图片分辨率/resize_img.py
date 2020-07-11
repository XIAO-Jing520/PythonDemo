# -*- coding: utf-8 -*-

from PIL import Image
import glob
import os
import sys
# 图片批处理

img_format = ['*.jpg', '*.png','*.jpeg']


def resize_write_img(bili, files, opfile, filterame, pic_format):
    im = Image.open(files)
    x, y = im.size

    im_ss = im.resize((int(x / bili), int(y / bili)))
    im_ss.save(opfile + filterame + pic_format)


def timage(argv, img_format):
    opfile = r'./resized/'
    # 输出路径
    # 判断opfile是否存在,不存在则创建
    if (os.path.isdir(opfile) == False):
        os.mkdir(opfile)

    if argv[1] == '--bili':
        bili = float(argv[2])
        for each_format in img_format:
            pic_format = each_format[1:]
            for files in glob.glob(each_format):
                filepath, filename = os.path.split(files)
                filterame, exts = os.path.splitext(filename)
                resize_write_img(bili, files, opfile,
                                 filterame, pic_format)
    else:
        for files in glob.glob('*.jpg'):
            filepath, filename = os.path.split(files)
            filterame, exts = os.path.splitext(filename)

            im = Image.open(files)
            im_ss = im.resize((int(argv[1]), int(argv[2])))
            im_ss.save(opfile + filterame + '.jpg')


if __name__ == '__main__':
    timage(sys.argv, img_format)
