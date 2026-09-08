import os
from PIL import Image

def resize_image(input_image_path, output_folder, max_size=1365):
    # 打开图片
    img = Image.open(input_image_path)

    width, height = img.size
    if max(width, height) > max_size:
        ratio = max_size / max(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        img = img.resize((new_width, new_height))

    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 获取输出文件路径
    filename = os.path.basename(input_image_path)
    output_image_path = os.path.join(output_folder, filename)

    # 保存调整大小后的图像
    img.save(output_image_path)

def resize_images_in_folder(input_folder, output_folder):
    # 遍历目录中的每个文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 获取完整的文件路径
            input_image_path = os.path.join(input_folder, filename)
            # 调整图片大小并保存到输出文件夹
            resize_image(input_image_path, output_folder)

    # 打印成功消息
    print("Success")

# 使用方法
resize_images_in_folder('C:/Users/1/OneDrive/桌面/tepp', 'C:/Users/1/OneDrive/桌面/datasets(10)')
