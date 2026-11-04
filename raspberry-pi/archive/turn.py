import os
import shutil
import random

# 原始数据目录和目标目录
train_images_dir = "D:/Library_seat_query/library/datasets(11)/train/images"
train_labels_dir = "D:/Library_seat_query/library/datasets(11)/train/labels"

validation_images_dir = "D:/Library_seat_query/library/datasets(11)/val/images"
validation_labels_dir = "D:/Library_seat_query/library/datasets(11)/val/labels"
test_images_dir = "D:/Library_seat_query/library/datasets(11)/test/images"
test_labels_dir = "D:/Library_seat_query/library/datasets(11)/test/labels"



# 获取所有图片文件名
all_images = os.listdir(train_images_dir)

# 创建一个字典来存储每个图片对应的标签文件名
image_to_label = {}
for image in all_images:
    image_name = image.split(".")[0]  # 去除文件扩展名
    label_file = image_name + ".txt"  # 对应的标签文件
    image_to_label[image] = label_file

# 确定要移动到验证集和测试集的比例
validation_ratio = 0.2  # 将20%的图片移动到验证集
test_ratio = 0.05  # 将5%的图片移动到测试集

# 获取要移动的图片列表
all_images = list(image_to_label.keys())
random.shuffle(all_images)  # 打乱图片顺序

num_validation = int(len(all_images) * validation_ratio)
num_test = int(len(all_images) * test_ratio)

validation_images = all_images[:num_validation]
test_images = all_images[num_validation:num_validation + num_test]

# 移动图片到验证集和测试集目录，并复制对应的标签文件
for image in validation_images:
    src_image = os.path.join(train_images_dir, image)
    dst_image = os.path.join(validation_images_dir, image)
    shutil.move(src_image, dst_image)

    src_label = os.path.join(train_labels_dir, image_to_label[image])
    dst_label = os.path.join(validation_labels_dir, image_to_label[image])
    shutil.move(src_label, dst_label)

for image in test_images:
    src_image = os.path.join(train_images_dir, image)
    dst_image = os.path.join(test_images_dir, image)
    shutil.move(src_image, dst_image)

    src_label = os.path.join(train_labels_dir, image_to_label[image])
    dst_label = os.path.join(test_labels_dir, image_to_label[image])
    shutil.move(src_label, dst_label)

# 最后，您可能需要将剩余的图片留在训练集中
# 或者将它们也移动到验证集或测试集中，取决于您的具体需求
