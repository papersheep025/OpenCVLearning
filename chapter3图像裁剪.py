# @FileName  :chapter3.py
# @Time      :2023/3/28 16:58
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

img = cv2.imread('Resources/Lena.jpg')
imgResize = cv2.resize(img, (600, 600))  # 调整像素数量，但是不裁剪
imgCropped = img[0:200, 0:300]  # 以左上角为基准裁剪，[起点：终点,起点：终点]

cv2.imshow('originalena', img)
cv2.imshow('600x600lena', imgResize)
cv2.imshow('Croppedimg', imgCropped)

# 查询像素量，显示（长，宽，通道数）
print(img.shape)
print(imgResize.shape)

cv2.waitKey(0)
