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
    time.sleep(60)

# 释放摄像头
cap.release()



# id
import time
import cv2
from ultralytics import YOLO
from collections import Counter
import requests
import json

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 设备ID
device_id = 'device_1'

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

        # 创建要发送的数据
        data = {
            'device_id': device_id,
            'counts': dict(counter)
        }

        # 将数据转换为 JSON 格式
        data = json.dumps(data)

        # 发送 HTTP 请求
        response = requests.post('http://your-server.com/api/path', data=data)
    else:
        print("无法获取摄像头画面")

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()








# id
import time
import cv2
from ultralytics import YOLO
from collections import Counter
import requests
import json

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 从文件中读取设备ID
with open('device_id.txt', 'r') as file:
    device_id = file.read().strip()

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

        # 创建要发送的数据
        data = {
            'device_id': device_id,
            'counts': dict(counter)
        }

        # 将数据转换为 JSON 格式
        data = json.dumps(data)

        # 发送 HTTP 请求
        response = requests.post('http://your-server.com/api/path', data=data)
    else:
        print("无法获取摄像头画面")

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()





import time
import cv2
from ultralytics import YOLO
from collections import Counter
import requests
import json

# 初始化YOLO模型
model = YOLO('D:/Library_seat_query/library/detect/train/weights/best.pt')

# 从文件中读取设备ID
with open('device_id.txt', 'r') as file:
    device_id = file.read().strip()

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

        # 创建要发送的数据
        data = {
            'device_id': device_id,
            'counts': dict(counter)
        }

        # 将数据转换为 JSON 格式
        data = json.dumps(data)

        # 发送 HTTP 请求
        response = requests.post('<SERVER_HOST>:8000/update_data', data=data)
        
        # 检查响应状态码
        if response.status_code == 200:
            print("请求成功")
        elif response.status_code == 404:
            print("请求的资源未找到")
        elif response.status_code == 500:
            print("服务器内部错误")
        else:
            print("请求失败，状态码：", response.status_code)

    else:
        print("无法获取摄像头画面")

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()