# @FileName  :excersice.py
# @Time      :2023/3/28 17:37
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

imgTaffy = cv2.imread('Resources/Taffy.png')
imgResizedTaffy = cv2.resize(imgTaffy,(400,400))
imgHaoSiMiao = cv2.cvtColor(imgResizedTaffy,cv2.COLOR_BGR2GRAY)

cv2.imshow('Taffy',imgResizedTaffy)
cv2.imshow('HaoSiMiao',imgHaoSiMiao)

cv2.waitKey(0)