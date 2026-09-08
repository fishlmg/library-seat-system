import cv2
import os
import time

# 设置保存图片的文件夹路径
save_folder = '/home/pi/Desktop/images'


# 打开摄像头
cap = cv2.VideoCapture(0)

# 设置图片编号
img_counter = 0

# 设置最大的图片数量
max_images = 10

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 生成图片文件名
        img_name = os.path.join(save_folder, "opencv_frame_{}.png".format(img_counter))
        # 将图片保存为文件
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
    else:
        print("无法获取摄像头画面")

    # 如果达到最大的图片数量，结束循环
    if img_counter >= max_images:
        break

    # 暂停一段时间（例如，600秒即10分钟）
    time.sleep(60)

# 释放摄像头
cap.release()