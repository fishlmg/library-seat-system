# 图书馆座位检测与发布系统

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)](https://flask.palletsprojects.com/)
[![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-00ffff.svg)](https://github.com/ultralytics/ultralytics)

一套完整的**图书馆座位实时发布系统**：树莓派 + 摄像头通过 YOLO 目标检测自动统计座位占用，上报到云服务器（Flask + PostgreSQL），网页端实时展示各区域空余座位数，方便同学快速找座。

## 🏗 系统架构

```
┌──────────────────────┐   HTTP POST    ┌─────────────────────┐   查询    ┌──────────┐
│  树莓派 + 摄像头      │ ─────────────▶ │  云服务器            │ ────────▶ │  浏览器   │
│  YOLO 座位检测        │  /update_data  │  Flask + PostgreSQL  │  /query   │  实时页面 │
│  (raspberry-pi/)     │  (带密码鉴权)   │  (server/)          │  JSON/HTML │          │
└──────────────────────┘                └─────────────────────┘           └──────────┘
```

## ✨ 特性

- **边缘检测**：树莓派端 YOLO 实时检测座位占用（occupied / available）
- **定时上报**：检测结果按周期 POST 到服务器，接口密码鉴权
- **数据持久化**：Flask-SQLAlchemy 写入 PostgreSQL，按区域分表
- **网页展示**：座位查询页、图书推荐页、相关信息页
- **API 支持**：`/query` 根据 `Accept: application/json` 返回 JSON，便于对接其他端
- **容器化**：提供 Dockerfile，一键部署后端

## 🗂 项目结构

```
.
├── server/                         # Flask 后端（云服务器）
│   ├── app.py                      # 路由、数据模型、上报鉴权、查询 API
│   ├── requirements.txt
│   ├── Dockerfile                  # 容器化部署
│   ├── .env.example                # 环境变量模板（PASSWORD / DB_HOST）
│   ├── templates/                  # Jinja2 页面模板
│   │   ├── index.htm               # 首页
│   │   ├── seat_query.htm          # 座位查询页（核心）
│   │   ├── books_recommendation.htm
│   │   └── related_information.htm
│   └── static/                     # 静态资源（轮播图等网页素材）
│
└── raspberry-pi/                   # 检测端（树莓派）
    ├── camera.py                   # 摄像头检测 + 上报（主程序）
    ├── camera_without_saving.py    # 不落盘版本
    ├── pt_to_onnx.py               # 模型转换（PyTorch → ONNX）
    ├── requirements.txt
    ├── .env.example                # 环境变量模板（上报地址与密码）
    ├── raspberrypi/                # 外设脚本（预览、拍照、录像；原 rassberyypi/）
    └── archive/                    # 迭代脚本与试验，不是部署入口
```

## 🚀 后端部署（server/）

```bash
cd server
pip install -r requirements.txt
cp .env.example .env        # 填写 PASSWORD 与 DB_HOST
python app.py               # 监听 0.0.0.0:5000
```

或使用 Docker：

```bash
docker build -t seat-server .
docker run -p 5000:5000 --env-file .env seat-server
```

**环境变量：**

| 变量 | 说明 |
| --- | --- |
| `PASSWORD` | 数据上报接口密码（树莓派端需一致） |
| `DB_HOST` | PostgreSQL 数据库地址 |

**API：**

| 路由 | 方法 | 说明 |
| --- | --- | --- |
| `/query` | GET | 页面（HTML）或 `Accept: application/json` 时返回各区域座位 JSON |
| `/update_data_1` | POST | 区域 1 数据上报（需 password 字段） |
| `/update_data_2` | POST | 区域 2 数据上报 |

## 📷 检测端部署（raspberry-pi/）

```bash
cd raspberry-pi
pip install -r requirements.txt
cp .env.example .env        # 填写 SEAT_SERVER_HOST / SEAT_SERVER_PASSWORD
python camera.py            # 启动摄像头检测并上报
```

上报只走上面的 `camera.py`（或不落盘的 `camera_without_saving.py`）。`archive/` 是早期原型、计数和数据集缩放试验；`raspberrypi/` 是预览、拍照、录像等外设脚本。两个目录都有自己的说明文件。

**环境变量：**

| 变量 | 说明 |
| --- | --- |
| `SEAT_SERVER_HOST` | 后端服务地址（域名或 IP） |
| `SEAT_SERVER_PASSWORD` | 上报密码（与后端 `PASSWORD` 一致） |

## 🔒 安全说明

- 所有服务器地址、数据库地址、接口密码均通过**环境变量**配置，代码中无硬编码
- 上报接口使用密码鉴权，密码不落盘到仓库（参照 `.env.example` 配置）

## 📝 说明

- YOLO 模型权重（`.pt` / `.onnx`）、训练数据集与训练输出不包含在仓库中（`.gitignore` 已排除）
- 开发过程中的原型脚本已移到 `raspberry-pi/archive/`。三份图片缩放脚本（原 `cahnge_the_size.py`、`changesizes.py`、`resize_2.py`）规则不同，只改名、不合并，对照见该目录说明
- `pt_to_onnx.py` 里的 `D:/Library_seat _query/rassberyypi` 是当时的本机导出目录，不是本仓库路径，本次未改脚本

## 🔗 相关项目

- [yolo-seat-detection](https://github.com/fishlmg/yolo-seat-detection)：图书馆座位占用检测模型的训练、评估与 ONNX 导出。本仓库的树莓派端加载其权重做摄像头推理和结果上报，网页与数据库在 `server/`。

## 📄 许可证

[MIT License](LICENSE)
