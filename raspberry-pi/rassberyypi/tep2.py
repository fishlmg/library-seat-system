import time
import cv2
from ultralytics import YOLO
from collections import Counter

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 进行推理
        predictions = model.predict(frame, save=False, imgsz=640, conf=0.5)

        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])
        print(counter)
    else:
        print("无法获取摄像头画面")

    # 暂停一段时间
    time.sleep(10)

# 释放摄像头
cap.release()