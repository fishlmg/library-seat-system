import os
from ultralytics import YOLO

model = YOLO('D:/Library_seat _query/yoloruns/train3/weights/best.pt')
folder = 'C:/Users/1/OneDrive/桌面/schlibrary/3.8'  # Specify the folder path here

# Iterate over all files in the folder
for filename in os.listdir(folder):
    file = os.path.join(folder, filename)
      # 进行推理
    results = model.predict(folder, save=False, imgsz=640, conf=0.5,iou=0.5)
    # View results
for r in results:
    print(r.boxes)  # print the Boxes object containing the detection bounding boxes

    
