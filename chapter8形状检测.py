# @FileName  :chapter8形状检测.py
# @Time      :2023/3/29 12:51
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

# 图像堆叠函数
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


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
            # 显示3的是三角形，显示4的是四边形，超过4的是圆
            print(len(approx))
            objCor = len(approx)
            # 获取图形的边框数据
            x, y, w, h = cv2.boundingRect(approx)
            # 利用边框数据画出方形边框
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # 如果检测到的是三角形
            if objCor == 3:
                objectType = 'Tri'
            # 如果检测到的是四边形
            elif objCor == 4:
                aspRatio = w / float(h)
                # 通过长宽比确定是正方形还是长方形
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = 'Square'
                else:
                    objectType = 'Rectangle'
            # 在图中，检测到大于4的即为圆
            elif objCor > 4:
                objectType = 'Circles'
            else:
                objectType = 'None'

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 0), 2)




path = 'Resources/bacteria3.png'

img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (5, 5), 1)
imgCanny = cv2.Canny(img, 50, 50)
# 创建一个全黑的图像
imgBlank = np.zeros_like(img)

getContours(imgCanny)

imgStack = stackImages(0.5, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
cv2.imshow('Images', imgStack)

cv2.waitKey(0)
