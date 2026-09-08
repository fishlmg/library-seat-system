import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
import requests

# 初始化YOLO模型
model = YOLO('D:/Library_seat_query/detection/train4/train4/weights/best.pt')
cap = cv2.VideoCapture(0)

# 打开文本文件并从中读取Flask应用程序的地址
with open('请在该文档中更改网页地址与设备序列.txt', 'r') as file:
    lines = file.readlines()
    # 获取第一行的地址信息并去除空白字符
    url = lines[0].strip()

while True:
    if not cap.isOpened(): 
        print('无法打开摄像头')
        break
    ret, frame = cap.read()
    if ret:
        results = model.predict(frame, conf=0.5, save=False, imgsz=640, iou=0.5)
        class_names = model.names
        class_counts = defaultdict(int)

        for result in results:
            # 获取检测框对象
            boxes = result.boxes
            
            # 循环遍历每个检测框
            for i in range(len(boxes)):
                # 获取当前检测框的类别索引
                class_index = int(boxes.cls[i])
                
                # 使用类别索引获取类别名称
                class_name = class_names[class_index]

                # 增加对应类别的计数
                class_counts[class_name] += 1

        # 发送POST请求
        response = requests.post(url, json=class_counts)

        # 检查响应状态码
        if response.status_code == 200:
            print("请求成功")
        elif response.status_code == 404:
            print("请求的资源未找到")
        elif response.status_code == 500:
            print("服务器内部错误")
        else:
            print("请求失败，状态码：", response.status_code)

    print("无法获取摄像头画面")
   
    # 重置类别计数，准备处理下一帧
    class_counts = defaultdict(int)

    # 拍摄周期
    time.sleep(600)

cap.release()