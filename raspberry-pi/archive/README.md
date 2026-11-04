# 归档：检测端迭代脚本

这里存放树莓派端从原型到部署过程中的试验代码和命令笔记。**不要用这些文件做部署。**

正式入口在上一级目录：

| 文件 | 用途 |
| --- | --- |
| `../camera.py` | 摄像头检测并上报（主程序） |
| `../camera_without_saving.py` | 同上，检测结果不落盘 |
| `../pt_to_onnx.py` | 把 PyTorch 权重量导出为 ONNX |
| `../requirements.txt` | 依赖 |
| `../.env.example` | 上报地址与密码模板 |

脚本正文未改。其中的绝对路径（如 `D:/Library_seat_query/...`、`/home/pi/...`）是当时本机目录，只作历史记录。

## 图片缩放（三份未合并）

三份脚本都在改数据集图片尺寸，但规则不同，合并会改变其中某一份的行为，因此只修正文件名：

| 现文件名 | 原文件名 | 行为 |
| --- | --- | --- |
| `resize_to_fixed.py` | `cahnge_the_size.py` | 全部缩放到固定尺寸（调用处为 1365×1024），写到输出目录 |
| `resize_by_orientation.py` | `changesizes.py` | 横图 1365×1024、竖图 1024×1365，覆盖原文件 |
| `resize_max_side.py` | `resize_2.py` | 长边超过 1365 时按比例缩小，写到另一目录 |

## 其余文件

| 文件 | 内容 |
| --- | --- |
| `3.py` | 对单张图片做一次 YOLO 推理并数 occupied / available |
| `b.py` | 摄像头 + YOLO 计数的两段草稿 |
| `new.py` | 带上报的摄像头检测原型 |
| `comp.py` | 摄像头检测草稿；后半段从文本读取上报地址 |
| `shift.py` | 摄像头检测，上报地址从文本文件读取 |
| `hzx.py` | 统计各类别数量并打印 JSON |
| `hzx2.py` | 在 `hzx.py` 基础上向 Flask 发 POST |
| `count.py` | 按类别计数的小函数 |
| `count1.py` | 从检测结果里数 occupied / available |
| `oldtest.py` | 遍历文件夹做推理 |
| `results.py` | 遍历文件夹做推理并整理结果 |
| `tp.py` | 监视目录中的新图片并推理（早期长脚本） |
| `check.py` | 检查训练集图片与标签是否一一对应 |
| `turn.py` | 把训练集划出验证集 / 测试集 |
| `rename.py` | 按序号批量重命名图片 |
| `temp.txt` | 本机虚拟环境与 CUDA 安装笔记 |
| `yolocommand.txt` | 云 GPU 上的训练与拷贝命令笔记 |
| `GLIP/test.py` | GLIP 开放词汇检测试验，未接入上报链路 |

外设向的拍照、预览、录像脚本在 `../raspberrypi/`（由拼写错误的 `rassberyypi/` 改名而来）。
