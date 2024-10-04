# @FileName  :langya_task1.py
# @Time      :2023/7/8 15:16
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

img = cv2.imread('Resources/origin.png')
imgResize = cv2.resize(img, (640, 360))

pts1 = np.float32([[965, 151], [1693, 246], [227, 641], [1237, 989]])
pts2 = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (420, 594))

cv2.imshow('OriginalImage', imgResize)
cv2.imshow('PerspectiveImage', imgOutput)

cv2.waitKey(0)
