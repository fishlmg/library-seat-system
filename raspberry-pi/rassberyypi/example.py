import cv2
import time

def take_photo(camera_index, photo_filepath):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print('无法打开摄像头')
        return

    # 给摄像头一些时间来预热
    time.sleep(2)

    ret, frame = cap.read()
    if not ret:
        print('无法读取视频帧')
        return

    cv2.imwrite(photo_filepath, frame)

    cap.release()

# 使用索引为 0 的摄像头拍照，并将照片保存到 '/home/pi/Desktop/photo.jpg'
take_photo(0, '/home/pi/Desktop/photo.jpg')