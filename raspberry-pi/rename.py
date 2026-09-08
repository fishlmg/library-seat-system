import os
import shutil
def batch_rename(input_dir):
    files = os.listdir(input_dir)
    files.sort()  # 默认按字符串排序，这样文件名数字部分会按照顺序排序

    for index, old_name in enumerate(files):
        # 构建新的文件名，可以根据需要进行格式化
        new_name = f"{index+5000 + 1:03d}.jpg"  # 以三位数字格式进行命名，例如：001.jpg, 002.jpg, ...

        # 构建文件的完整路径
        old_path = os.path.join(input_dir, old_name)
        new_path = os.path.join(input_dir, new_name)

        # 重命名文件并覆盖原文件
        shutil.move(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    input_directory = "C:/Users/1/OneDrive/桌面/datasets(10)"
    batch_rename(input_directory)

