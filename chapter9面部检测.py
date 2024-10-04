# @FileName  :chapter9面部检测.py
# @Time      :2023/3/29 20:21
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
# 引入一个进行面部识别的级联分类器
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
img = cv2.imread('Resources/lena.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
# 在脸的周围形成边界框
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Result',img)
cv2.waitKey(0)