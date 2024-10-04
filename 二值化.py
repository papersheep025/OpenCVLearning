# @FileName  :二值化.py
# @Time      :2023/4/25 16:46
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0
import cv2

path = 'Resources/bacteria.jpg'

img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
height,width = imgGray.shape[0:2]
thresh = 180

for row in range(height):
    for col in range(width):
        gray = imgGray[row,col]
        if gray > thresh:
            imgGray[row,col] = 255
        elif gray <thresh:
            imgGray[row,col] = 0

cv2.imshow('img',imgGray)
cv2.waitKey(0)