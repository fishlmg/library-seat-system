

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
