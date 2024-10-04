# @FileName  :chapter2.py
# @Time      :2023/3/28 16:34
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpg')

kernel = np.ones((5, 5), np.uint8)  # 8bit图像

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 变灰
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)  # 图像模糊化处理     cv2.GaussianBlur（图像，高斯核的大小
imgCanny = cv2.Canny(img, 150, 200)  # 边缘检测    cv2.Canny（图像,阈值1，阈值2）
imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)  # 膨胀，将canny中的线条进行膨胀，并且迭代两次（在第一次基础上再加粗）
imgEroded = cv2.erode(imgDialation, kernel, iterations=2)  # 侵蚀，但进行相同次数的膨胀和侵蚀并不能回到原图像

cv2.imshow('Originimg', img)
cv2.imshow('Grayimg', imgGray)
cv2.imshow('Blurimg', imgBlur)
cv2.imshow('Cannyimg', imgCanny)
cv2.imshow('Dialationimg', imgDialation)
cv2.imshow('Erodedimg', imgEroded)

cv2.waitKey(0)
