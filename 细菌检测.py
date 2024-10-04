# @FileName  :细菌检测.py
# @Time      :2023/4/18 16:07
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2

# 边缘检测函数
def getContours(img):
    # cv2.findContours（图像，检索方法，轮廓近似方法）
    img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            # 绘制边缘
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            # 逼近角点
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # 角点检测数量超过4的是圆
            print(len(approx))
            objCor = len(approx)
            # 获取图形的边框数据
            x, y, w, h = cv2.boundingRect(approx)
            # 利用边框数据画出方形边框
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)

            if objCor > 4:
                objectType = 'Circles'
            else:
                objectType = 'None'



path = 'Resources/bacteria.jpg'

img = cv2.imread(path)
imgContour = img.copy()
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
