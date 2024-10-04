# @FileName  :video.py
# @Time      :2023/4/3 19:41
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0000000000000

import cv2
# 设置高度和宽度
frameWidth = 1920
frameHeight = 1080

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(20,200)

while True:
    success, img = cap.read()
    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

