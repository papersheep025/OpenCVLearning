# @FileName  :chapter6图像连接.py
# @Time      :2023/3/28 23:21
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpg')
# 横向连接
imgHorizontal = np.hstack((img,img))
# 纵向连接
imgVertical = np.vstack((img,img))

cv2.imshow('Horizontal',imgHorizontal)
cv2.imshow('Vertical',imgVertical)

cv2.waitKey(0)