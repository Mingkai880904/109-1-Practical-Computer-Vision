# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:05:27 2020

@author: 沈明楷
"""


from PIL import Image
from pylab import *
from scipy.ndimage import filters
import cv2


img = Image.open("../data/fig1a.jpg")#子图文件名
icon = Image.open("../data/fig1b.jpg")#子图文件名
icon2= Image.open("../data/fig1c.jpg")



icon = icon.resize((600, 300))
imshow(icon)

# 获取图片的宽高
img_w, img_h = img.size#获取被放图片的大小（母图）
icon_w,icon_h=icon.size#获取小图的大小（子图）
factor = 6
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
#防止子图尺寸大于母图

if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
# # 重新设置子图的尺寸
# icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 5)
h = int((img_h - icon_h) / 5)
# 粘贴图片
img.paste(icon, (250, 400), mask=None)
img.paste(icon2, (500, 300), mask=None)
img.paste(icon2, (600, 700), mask=None)
img.paste(icon2, (550, 600), mask=None)
img.paste(icon2, (500, 300), mask=None)
img.paste(icon2, (650, 750), mask=None)
img.paste(icon2, (750, 800), mask=None)
img.paste(icon2, (800, 750), mask=None)
img.paste(icon2, (900, 650), mask=None)
img.paste(icon2, (550, 600), mask=None)
axis('off')
# 保存图片
imshow(img)
img.save("../data/AAA.jpg")#合成后的图片路径以及文件名