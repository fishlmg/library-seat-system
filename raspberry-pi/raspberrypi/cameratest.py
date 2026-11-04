import cv2

def check_camera(index):
    cap = cv2.VideoCapture(index)
    if cap is None or not cap.isOpened():
        print('警告：无法打开视频捕获')
        return False
    else:
        print('摄像头正常')
        cap.release()
        return True

# 检查索引为 0 的摄像头
check_camera(0)