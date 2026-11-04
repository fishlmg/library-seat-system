import numpy as np

# 假设 predictions 是您提供的 ultralytics.engine.results.Results 对象
predictions = ...

# 初始化 occupied 和 available 的计数器
occupied_count = 0
available_count = 0

# 遍历预测结果中的边界框
for box in predictions.boxes:
    # 获取边界框的类别标签
    label = box.cls.item()
    
    # 根据类别标签更新计数器
    if label == 0:
        occupied_count += 1
    elif label == 1:
        available_count += 1

print(f"occupied: {occupied_count}, available: {available_count}")
