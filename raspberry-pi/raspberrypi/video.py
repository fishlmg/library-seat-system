import picamera
import time

# 设置视频文件保存路径
video_path = '/home/pi/video.h264'

# 设置视频录制时长（秒）
record_duration = 10

# 初始化摄像头
with picamera.PiCamera() as camera:
    try:
        # 开始录制视频
        camera.start_recording(video_path)
        
        # 录制指定时长
        camera.wait_recording(record_duration)
        
        # 停止录制视频
        camera.stop_recording()
        
        print("视频已保存到:", video_path)
        
    except Exception as e:
        print("发生错误:", str(e))


        import picamera
import time
import keyboard

# 设置视频文件保存路径
video_path = '/home/pi/video.h264'

# 初始化摄像头
with picamera.PiCamera() as camera:
    try:
        # 开始录制视频
        camera.start_recording(video_path)
        
        # 持续录制直到按下 "h" 键
        while not keyboard.is_pressed('h'):
            pass
        
        # 停止录制视频
        camera.stop_recording()
        
        print("视频已保存到:", video_path)
        
    except Exception as e:
        print("发生错误:", str(e))

