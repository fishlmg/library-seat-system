import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 显示画面
        cv2.imshow('Camera', frame)

        # 如果按下q键，就退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("无法获取摄像头画面")
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()