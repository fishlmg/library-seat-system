import os
from PIL import Image

def resize_image(image_path):
    # 打开图片
    img = Image.open(image_path)

    # 检查图片是否为横屏拍摄
    if img.width > img.height:
        # 横屏拍摄，改变大小为1365*1024
        img = img.resize((1365, 1024))
    else:
        # 竖屏拍摄，改变大小为1024*1365
        img = img.resize((1024, 1365))

    # 覆盖原文件
    img.save(image_path)

def resize_images_in_folder(folder_path):
    # 遍历目录中的每个文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 获取完整的文件路径
            file_path = os.path.join(folder_path, filename)
            # 调整图片大小
            resize_image(file_path)

    # 打印成功消息
    print("Success")

# 使用方法
resize_images_in_folder('D:/Library_seat _query/library/datasets(7)/images')