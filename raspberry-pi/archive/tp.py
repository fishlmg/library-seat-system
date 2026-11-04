



import os
import time
import cv2
from ultralytics import YOLO

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 文件夹路径
folder = 'D:/Library_seat _query/Ntrain'
output_folder = '/home/pi/Desktop/yoloruns'

# 文件跟踪
files = set(os.listdir(folder))
no_new_files_counter = 0

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
        # 生成图片文件名
        img_name = os.path.join(folder, "opencv_frame_{}.png".format(len(files)))
        # 将图片保存为文件
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        # 进行推理
        predictions = model.predict(img_name, save=True, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
        print(predictions)

        # 更新文件集
        files.add(img_name)
    else:
        print("无法获取摄像头画面")

    # 检查新文件
    new_files = set(os.listdir(folder)) - files

    if new_files:
        # 重置计数器
        no_new_files_counter = 0

        # 遍历新文件
        for filename in new_files:
            file = os.path.join(folder, filename)
            output_file = os.path.join(output_folder, filename)
            predictions = model.predict(file, save=True, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
            print(predictions)

        # 更新文件集
        files.update(new_files)
    else:
        # 增加计数器
        no_new_files_counter += 1

        # 检查计数器是否达到100
        if no_new_files_counter >= 100:
            break

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()


#1
import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
import requests

# 初始化YOLO模型
model = YOLO('/home/pi/Desktop/best.pt')
cap = cv2.VideoCapture(0)

# 打开文本文件并从中读取Flask应用程序的地址
with open('请在该文档中更改设备序列.txt', 'r') as file:
    lines = file.readlines()
    # 获取第一行的地址信息并去除空白字符
    id = lines[0].strip()
    url = f"http://<SERVER_HOST>:8000/update_{id}"
#print(url)

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
            if class_counts=={}:
                print("No objects detected")
                class_counts={"occupied":0, "available":0}
            elif len(class_counts)==1:
                if "occupied" in class_counts:
                    class_counts["available"]=0
                elif "available" in class_counts:
                    class_counts["occupied"]=0
        print(class_counts)

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

    #print("无法获取摄像头画面")
   
    # 重置类别计数，准备处理下一帧
    class_counts = defaultdict(int)

    # 拍摄周期
    time.sleep(20)

cap.release()













import os
import time
import cv2
from ultralytics import YOLO
from collections import Counter

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 文件夹路径
folder = 'D:/Library_seat _query/Ntrain'
output_folder = '/home/pi/Desktop/yoloruns'

# 文件跟踪
files = set(os.listdir(folder))
no_new_files_counter = 0

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
        # 生成图片文件名
        img_name = os.path.join(folder, "opencv_frame_{}.png".format(len(files)))
        # 将图片保存为文件
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        # 进行推理
        predictions = model.predict(img_name, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
        
        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])
        print(counter)

        # 更新文件集
        files.add(img_name)
    else:
        print("无法获取摄像头画面")

    # 检查新文件
    new_files = set(os.listdir(folder)) - files

    if new_files:
        # 重置计数器
        no_new_files_counter = 0

        # 遍历新文件
        for filename in new_files:
            file = os.path.join(folder, filename)
            output_file = os.path.join(output_folder, filename)
            predictions = model.predict(file, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
            
            # 计数每种类别的数量
            counter = Counter([pred['name'] for pred in predictions])
            print(counter)

        # 更新文件集
        files.update(new_files)
    else:
        # 增加计数器
        no_new_files_counter += 1

        # 检查计数器是否达到100
        if no_new_files_counter >= 100:
            break

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()







# 网页版

import os
import time
import cv2
from ultralytics import YOLO
from collections import Counter
import requests
import json

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 文件夹路径
folder = 'D:/Library_seat _query/Ntrain'
output_folder = '/home/pi/Desktop/yoloruns'

# 文件跟踪
files = set(os.listdir(folder))
no_new_files_counter = 0

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
        # 生成图片文件名
        img_name = os.path.join(folder, "opencv_frame_{}.png".format(len(files)))
        # 将图片保存为文件
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        # 进行推理
        predictions = model.predict(img_name, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
        
        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])
        print(counter)

        # 将结果转换为 JSON 格式
        data = json.dumps(counter)

        # 发送 HTTP 请求
        response = requests.post('http://your-server.com/api/path', data=data)

        # 更新文件集
        files.add(img_name)
    else:
        print("无法获取摄像头画面")

    # 检查新文件
    new_files = set(os.listdir(folder)) - files

    if new_files:
        # 重置计数器
        no_new_files_counter = 0

        # 遍历新文件
        for filename in new_files:
            file = os.path.join(folder, filename)
            output_file = os.path.join(output_folder, filename)
            predictions = model.predict(file, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
            
            # 计数每种类别的数量
            counter = Counter([pred['name'] for pred in predictions])
            print(counter)

            # 将结果转换为 JSON 格式
            data = json.dumps(counter)

            # 发送 HTTP 请求
            response = requests.post('http://your-server.com/api/path', data=data)

        # 更新文件集
        files.update(new_files)
    else:
        # 增加计数器
        no_new_files_counter += 1

        # 检查计数器是否达到100
        if no_new_files_counter >= 100:
            break

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

        # 将结果转换为 JSON 格式
        data = json.dumps(counter)

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









#3.8count
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

        # 计算occupied和available的数量
        occupied_count = counter.get('occupied', 0)
        available_count = counter.get('available', 0)

        # 创建要发送的数据
        data = {
            'device_id': device_id,
            'occupied_count': occupied_count,
            'available_count': available_count
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











from ultralytics import YOLO
 
# 加载模型
model = YOLO('D:/Library_seat _query/yoloruns/train3/weights/best.pt')
 
# 摄像头编号
#camera_no = 0
 
# 打开摄像头
#cap = cv2.VideoCapture(camera_no)
 
#while cap.isOpened():
    # 获取图像
    #res, frame = cap.read()
 
    # 如果读取成功
   # if res:
        # 正向推理
results = model("C:/Users/1/OneDrive/桌面/schlibrary/101MEDIA/DJI_0154.JPG")
 
        # 绘制结果
#annotated_frame = results[5].plot()
 
        # 获取检测到的物体的数量
for r in results:
    print(r.names[r.boxes.cls[0].item( )])
#num_classes = len(results.names)
#print(f"Number of classes: {num_classes}")

 
       

       







from ultralytics import YOLO
 
# 加载模型
model = YOLO('D:/Library_seat _query/yoloruns/train3/weights/best.pt')
 
# 摄像头编号
#camera_no = 0
 
# 打开摄像头
#cap = cv2.VideoCapture(camera_no)
 
#while cap.isOpened():
    # 获取图像
    #res, frame = cap.read()
 
    # 如果读取成功
   # if res:
        # 正向推理
results = model("C:/Users/1/OneDrive/桌面/schlibrary/100MEDIA/DJI_0959.JPG")
 
        # 绘制结果
#annotated_frame = results[5].plot()
 
        # 获取检测到的物体的数量
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

print(f"occupied: {occupied}, available: {available}")







from ultralytics import YOLO
 
# 加载模型
model = YOLO('D:/Library_seat _query/yoloruns/train3/weights/best.pt')
source_folder = 'C:/Users/1/OneDrive/桌面/schlibrary/100MEDIA/DJI_0956.JPG'

results = model(source_folder,save=False, imgsz=640, conf=0.5,iou=0.5)
 
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

print(f"occupied: {occupied}, available: {available}")



#3.9
import time
import cv2
from ultralytics import YOLO
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


#Shoot cycles
time.sleep(60)

cap.release()



#3,13
import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
#import json
import requests

model = YOLO('D:/Library_seat_query/detection/train4/train4/weights/best.pt')
cap = cv2.VideoCapture(0)

while True :

    if not cap.isOpened(): 
        print('无法打开摄像头')
        break
    ret,frome =cap.read()
    if ret:

        results = model.predict(frome,conf=0.5,save=False, imgsz=640, iou=0.5)
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

# 将字典转换为JSON格式字符串
#json_string = json.dumps(class_counts)

# 打印JSON格式字符串
#print(json_string)

# 设置Flask应用程序的地址
url = 'http://<SERVER_HOST>:8000/update_data_1'

# 发送POST请求
response = requests.post(url, json=class_counts)


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
   
    # 重置类别计数，准备处理下一帧
class_counts = defaultdict(int)

#Shoot cycles
time.sleep(60)

cap.release()
# 打印响应
#print(response)



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




#good
import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
import requests

# 初始化YOLO模型
model = YOLO('/home/pi/Desktop/best.pt')
cap = cv2.VideoCapture(0)

# 打开文本文件并从中读取Flask应用程序的地址
with open('请在该文档中更改网页地址与设备序列.txt', 'r') as file:
    lines = file.readlines()
    # 获取第一行的地址信息并去除空白字符
    url = lines[0].strip()
#print(url)

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
            if class_counts=={}:
                print("No objects detected")
                class_counts={"occupied":0, "available":0}
            elif len(class_counts)==1:
                if "occupied" in class_counts:
                    class_counts["available"]=0
                elif "available" in class_counts:
                    class_counts["occupied"]=0
        print(class_counts)

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

    #print("无法获取摄像头画面")
   
    # 重置类别计数，准备处理下一帧
    class_counts = defaultdict(int)

    # 拍摄周期
    time.sleep(20)

cap.release()


import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
import requests

# 初始化YOLO模型
model = YOLO('/home/pi/Desktop/best.pt')
cap = cv2.VideoCapture(0)

# 打开文本文件并从中读取Flask应用程序的地址
with open('请在该文档中更改设备序列.txt', 'r') as file:
    lines = file.readlines()
    # 获取第一行的地址信息并去除空白字符
    id = lines[0].strip()
    url = f"http://<SERVER_HOST>:8000/update_data_{id}"
#print(url)

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
            if class_counts=={}:
                print("No objects detected")
                class_counts={"occupied":0, "available":0}
            elif len(class_counts)==1:
                if "occupied" in class_counts:
                    class_counts["available"]=0
                elif "available" in class_counts:
                    class_counts["occupied"]=0
        print(class_counts)

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

    #print("无法获取摄像头画面")
   
    # 重置类别计数，准备处理下一帧
    class_counts = defaultdict(int)
    

    # 拍摄周期
    time.sleep(20)

cap.release()


import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
import requests
import os

password = os.getenv("PASSWORD")

# 初始化YOLO模型
model = YOLO('/home/pi/Desktop/best.pt')
cap = cv2.VideoCapture(0)

# 打开文本文件并从中读取Flask应用程序的地址
with open('请在该文档中更改设备序列.txt', 'r') as file:
    lines = file.readlines()
    # 获取第一行的地址信息并去除空白字符
    id = lines[0].strip()
    url = f"http://<SERVER_HOST>:8000/update_data_{id}"
#print(url)

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
            if class_counts=={}:
                print("No objects detected")
                class_counts={"occupied":0, "available":0}
            elif len(class_counts)==1:
                if "occupied" in class_counts:
                    class_counts["available"]=0
                elif "available" in class_counts:
                    class_counts["occupied"]=0
        print(class_counts)
        class_counts['password'] = password
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

    #print("无法获取摄像头画面")
   
    # 重置类别计数，准备处理下一帧
    class_counts = defaultdict(int)
    
    # 拍摄周期
    time.sleep(20)

cap.release()



import time
import cv2
from collections import defaultdict
from ultralytics import YOLO
import requests
import os

password = os.getenv("PASSWORD")

# 初始化YOLO模型
model = YOLO('/home/pi/Desktop/best.pt')
cap = cv2.VideoCapture(0)

# 打开文本文件并从中读取Flask应用程序的地址
with open('请在该文档中更改设备序列.txt', 'r') as file:
    lines = file.readlines()
    # 获取第一行的地址信息并去除空白字符
    id = lines[0].strip()
    url = f"http://<SERVER_HOST>:8000/update_data_{id}"
#print(url)

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
            if class_counts=={}:
                print("No objects detected")
                class_counts={"occupied":0, "available":0}
            elif len(class_counts)==1:
                if "occupied" in class_counts:
                    class_counts["available"]=0
                elif "available" in class_counts:
                    class_counts["occupied"]=0
        print(class_counts)
        class_counts['password'] = password
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

    #print("无法获取摄像头画面")
   
    # 重置类别计数，准备处理下一帧
    class_counts = defaultdict(int)
    
    # 拍摄周期
    time.sleep(20)

cap.release()