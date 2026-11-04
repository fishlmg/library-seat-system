import os

# 训练集中的图片和标签目录
train_images_dir = "D:/Library_seat_query/library/datasets(11)/train/images"
train_labels_dir = "D:/Library_seat_query/library/datasets(11)/train/labels"

# 获取所有图片文件名和标签文件名
image_files = os.listdir(train_images_dir)
label_files = os.listdir(train_labels_dir)

# 检查每个图片文件是否有对应的标签文件
missing_labels = []
for image_file in image_files:
    # 构建对应的标签文件名
    label_file = image_file.split('.')[0] + ".txt"
    # 检查标签文件是否存在
    if label_file not in label_files:
        missing_labels.append(image_file)

# 检查每个标签文件是否有对应的图片文件
missing_images = []
for label_file in label_files:
    # 构建对应的图片文件名
    image_file = label_file.split('.')[0] + ".jpg"
    # 检查图片文件是否存在
    if image_file not in image_files:
        missing_images.append(label_file)

# 删除缺失的文件
for file_name in missing_labels:
    file_path = os.path.join(train_images_dir, file_name)
    if file_name=="classes.txt":
        continue
    else:
        #os.unlink(file_path)
        continue

for file_name in missing_images:
    file_path = os.path.join(train_labels_dir, file_name)
    #os.unlink(file_path)

# 输出结果
if missing_labels:
    print("以下图片文件缺少对应的标签文件：")
    for image_file in missing_labels:
        print(image_file)

if missing_images:
    print("\n以下标签文件缺少对应的图片文件:")
    for label_file in missing_images:
        print(label_file)

if not missing_labels and not missing_images:
    print("所有图片文件都有对应的标签文件，且所有标签文件都有对应的图片文件。")
