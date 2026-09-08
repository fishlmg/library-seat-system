# 图书馆座位检测与发布系统

一套完整的图书馆座位实时发布系统：树莓派 + 摄像头通过 YOLO 目标检测统计座位占用情况，上报到 Flask 后端写入 PostgreSQL，网页端实时展示各区空余座位数。

## 系统架构

```
树莓派 + 摄像头                     云服务器                         浏览器
┌─────────────────┐   HTTP POST   ┌─────────────────┐   GET/JSON   ┌──────────┐
│ YOLO 座位检测    │ ───────────▶ │ Flask + Postgres │ ───────────▶ │ 网页展示  │
│ (raspberry-pi/)  │  /update_data │ (server/)       │   /query     │ seat_query│
└─────────────────┘               └─────────────────┘              └──────────┘
```

## server/ — Flask 后端

- `app.py`：座位数据接收、查询 API、网页渲染
- `templates/`：座位查询、图书推荐、相关信息页面
- `static/`：网页静态资源（轮播图片等）
- `Dockerfile`：容器化部署

启动：

```bash
cd server
pip install -r requirements.txt
cp .env.example .env   # 填写 PASSWORD 和 DB_HOST
python app.py          # 0.0.0.0:5000
```

环境变量：

| 变量 | 说明 |
| --- | --- |
| `PASSWORD` | 数据上报接口密码（树莓派端需一致） |
| `DB_HOST` | PostgreSQL 地址 |

## raspberry-pi/ — 检测端

- YOLO 模型检测座位占用（`camera.py`、`tp.py` 等）
- 检测结果定时上报服务器（`url.py`）
- 包含模型转换（`pt_to_onnx.py`）、树莓派拍照/视频脚本（`rassberyypi/`）

部署：

```bash
cd raspberry-pi
pip install -r requirements.txt
cp .env.example .env   # 填写 SEAT_SERVER_HOST 和 SEAT_SERVER_PASSWORD
```

## 说明

- 模型权重（`.pt` / `.onnx`）、训练数据集与训练输出不包含在仓库中（`.gitignore` 已排除），本地保留
- 所有服务器地址与密码均通过环境变量配置，代码中无硬编码
