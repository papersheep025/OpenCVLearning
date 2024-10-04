# @FileName  :langya_task2.py
# @Time      :2023/7/8 15:38
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np
import time

cap = cv2.VideoCapture('Resources/AutoAim.mp4')
ret, frame = cap.read()
cap_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



while (cap.isOpened()):
    ret, frame = cap.read()
    cap_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', cap_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break