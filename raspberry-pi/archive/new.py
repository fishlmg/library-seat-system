import time
import cv2
from ultralytics import YOLO
import requests
import json


model = YOLO('D:/Library_seat_query/library/detect/train/weights/best.pt')


with open('device_id.txt', 'r') as file:
    device_id = file.read().strip()


cap = cv2.VideoCapture(0)

while True:
    
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        
        results = model(frame,save=False, imgsz=640, conf=0.5,iou=0.5)
         
occupied = 0
available = 0

for r in results:
        for i in range(len(r.boxes.cls)):

                status = r.names[r.boxes.cls[i].item()]
                #print(status)
                
                if(status == "occupied"):
                        occupied+=1
                if(status == "available"):
                        available+=1

                # print(type(r.names[r.boxes.cls[i].item()]))
    
#num_classes = len(results.names)
#print(f"Number of classes: {num_classes}")

out_put = (f"occupied: {occupied}, available: {available}")

#data
data = {
    'device_id': device_id,
    'out_put': dict(out_put)
}

data = json.dumps(data)

response = requests.post('<SERVER_HOST>:8000/update_data', data=data)
        
#检查响应状态码
if response.status_code == 200:
    print("请求成功")
elif response.status_code == 404:
    print("请求的资源未找到")
elif response.status_code == 500:
    print("服务器内部错误")
else:
    print("请求失败，状态码：", response.status_code)

print("无法获取摄像头画面")

#Shoot cycles
time.sleep(60)

cap.release()
