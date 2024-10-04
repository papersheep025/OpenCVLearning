# @FileName  :chapter4.py
# @Time      :2023/3/28 17:19
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(300,300),(0,255,0),3)#划线              cv2.line（起点，终点，颜色（蓝，绿，红），线条宽度）BGR
cv2.rectangle(img,(0,0),(200,300),(0,0,255),5)#画长方形      cv2.rectangle(起点，终点，颜色，线条宽度）
cv2.circle(img,(400,100),60,(255,0,255),3)#画圆             cv2.circle(圆心位置，半径，颜色，线条宽度）
cv2.putText(img,'OPENCV',(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,150),3)#输入文字

cv2.imshow('Image',img)
cv2.waitKey(0)