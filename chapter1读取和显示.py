import cv2

# 读取与显示图像和视频
img = cv2.imread('Resources/lena.jpg', 0)  # 如果写 0就是黑白图像.写1就是原图像

cv2.imshow('lena', img)  # 显示图像

cv2.waitKey(0)  # 延迟显示,0代表一直显示，即使程序暂停，1000是1秒

cv2.imwrite('lena_gray.jpg', img)  # 保存黑白图像

cap = cv2.VideoCapture('Resources/demo_video.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()  # 读取
    cap_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 变为灰色视频
    cv2.imshow('frame', cap_gray)
    if cv2.waitKey(10) & 0xFF == ord('q'):  # 这个值越大视频播放速度越慢，后面一段表示按下键盘上的q键后退出
        break
