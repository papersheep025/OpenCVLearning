# @FileName  :chapter5.py
# @Time      :2023/3/28 17:56
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

img = cv2.imread('Resources/card.jpg')

# 原图中卡片的四个角点
pts1 = np.float32([[148, 80], [437, 114], [94, 247], [423, 288]])
# 变换后分别在左上、右上、左下、右下四个点
pts2 = np.float32([[0, 0], [320, 0], [0, 178], [320, 178]])
# 生成透视矩阵
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(320,178))

cv2.imshow('OriginalImage',img)
cv2.imshow('PerspectiveImage',imgOutput)
cv2.waitKey(0)