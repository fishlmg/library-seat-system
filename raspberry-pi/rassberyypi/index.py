import cv2

def check_camera_index():
    for index in range(10):
        cap = cv2.VideoCapture(index)
        if cap is None or not cap.isOpened():
            print('警告：无法打开索引号为 {} 的摄像头'.format(index))
        else:
            print('索引号为 {} 的摄像头正常'.format(index))
            cap.release()

check_camera_index()