# @FileName  :chapter7.py
# @Time      :2023/3/28 23:33
# @Author    :Papersheep


if __name__ == "__main__":
    run_code = 0

import cv2
import numpy as np

def empty(a):
    pass
# 图像堆栈函数，后面会将四个图像连接在一起
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

path = 'Resources/lambo.png'

# 创建一个轨迹栏
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,240)
# 色彩
cv2.createTrackbar('Hue Min','TrackBars',0,179,empty)
cv2.createTrackbar('Hue Max','TrackBars',19,179,empty)
# 饱和度
cv2.createTrackbar('Sat Min','TrackBars',110,255,empty)
cv2.createTrackbar('Sat Max','TrackBars',240,255,empty)
# 数值
cv2.createTrackbar('Val Min','TrackBars',153,255,empty)
cv2.createTrackbar('Val Max','TrackBars',255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # 读取轨迹栏的值
    h_min = cv2.getTrackbarPos('Hue Min','TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
    # 为掩膜添加最小和最大的限制
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    # 创建掩膜
    mask = cv2.inRange(imgHSV,lower,upper)
    # 通过mask和原图的与运算，得到掩膜在原图中的部分
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    # 0.6 表示缩放比例
    imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    cv2.waitKey(1)