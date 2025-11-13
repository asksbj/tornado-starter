# Tornado Web应用

这是一个基于 Tornado 框架构建的 Web 应用模板，提供清晰的目录结构与常用功能配置，可作为学习或生产项目的良好起点。

## 功能特性

- 🚀 基于 Tornado 6 的高性能异步 Web 服务器  
- 🎨 预置 Bootstrap 5 UI，默认支持响应式布局  
- 🔌 RESTful API 示例与 JSON 工具方法  
- 🛡️ 启用 XSRF 保护与安全 Cookie  
- 📝 模板渲染与静态资源服务  
- ⚙️ `.env` 环境变量支持  
- 🧪 API 回显测试接口
- ⚡ 内置 Redis 异步连接模块

## 项目结构

```
tornado_starter/
├── tornado_starter/
│   ├── __init__.py           # 包初始化
│   ├── __main__.py           # 支持 python -m tornado_starter
│   ├── app.py                # 应用入口与应用工厂
│   ├── config.py             # 路径常量与 Tornado settings
│   ├── routes.py             # 路由集中注册
│   └── handlers/             # 请求处理器
│       ├── __init__.py
│       ├── api.py
│       ├── base.py
│       └── main.py
├── templates/                # HTML 模板
│   ├── base.html
│   └── index.html
├── static/                   # 静态资源
│   ├── css/
│   ├── images/
│   └── js/
├── .env.example              # 环境变量示例
├── .gitignore
├── README.md
├── requirements.txt
├── run.py                    # 启动脚本（设置默认环境变量）
└── start.sh                  # 自动化启动脚本
```

## 快速开始

### 1. 安装依赖

```bash
# 创建并激活虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# 或
venv\Scripts\activate           # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 根据需要编辑 .env 中的端口、调试模式、密钥等
```

应用会自动尝试加载项目根目录的 `.env` 文件；缺省时使用预设默认值。

### 3. 启动应用

```bash
# 方法 1：模块方式运行（推荐）
python -m tornado_starter

# 方法 2：脚本运行
python run.py

# 方法 3：一键脚本（自动创建/激活虚拟环境）
./start.sh
```

默认监听地址为 `http://localhost:8888`，可通过 `APP_PORT` 环境变量调整。

## API 示例

- `GET /api/info`：获取应用信息与版本  
- `GET /api/status`：返回服务运行状态  
- `GET /api/users`：获取用户列表（可选 `limit` 参数）  
- `POST /api/echo`：回显请求体 JSON
- `POST /api/users`：创建新用户（需要 `name` 与 `email` 字段）

`POST /api/echo` 示例：

```http
POST /api/echo
Content-Type: application/json

{
  "message": "Hello Tornado!"
}
```

## 开发指南

### 新增处理器

1. 在 `tornado_starter/handlers/` 新建模块或类，继承 `BaseHandler` 或 `tornado.web.RequestHandler`。  
2. 在 `tornado_starter/routes.py` 中注册对应路由。  

```python
# tornado_starter/handlers/example.py
from .base import BaseHandler


class ExampleHandler(BaseHandler):
    def get(self):
        self.write_json({"message": "Hello from new handler!"})


# tornado_starter/routes.py
from .handlers import ApiHandler, MainHandler
from .handlers.example import ExampleHandler


def get_routes(static_path: str | None = None) -> list[tuple]:
    routes = [
        (r"/", MainHandler),
        (r"/api/(.*)", ApiHandler),
        (r"/example", ExampleHandler),
    ]
    ...
```

### 模板与静态资源

- 在 `templates/` 目录添加模板文件，并在处理器中调用 `self.render("template.html", **context)`。  
- 在 `static/` 目录放置 CSS/JS/图片等资源，可通过 `/static/...` 访问。  
- Redis 客户端可通过 `self.settings["redis"]` 获取，返回 `redis.asyncio.Redis` 对象，可在异步方法中直接使用 `await redis.get(...)`、`await redis.set(...)`。

## 配置选项

| 变量名       | 默认值  | 说明                         |
|-------------|---------|------------------------------|
| `APP_PORT`  | `8888`  | 服务监听端口                 |
| `APP_DEBUG` | `True`  | Tornado 调试模式             |
| `SECRET_KEY`| `your-secret-key-change-this` | Cookie 加密密钥（生产必须修改） |
| `MONGODB_URI` | `mongodb://localhost:27017` | MongoDB 连接串 |
| `MONGODB_DB`  | `tornado_starter`           | MongoDB 数据库名 |
| `REDIS_URL`   | `redis://localhost:6379/0`  | Redis 连接串 |

## 部署建议

### 生产环境

- 创建独立的 `.env`，配置生产环境端口、关闭调试、更新 `SECRET_KEY`。  
- 建议配合 Nginx/Traefik 等反向代理及 Supervisor/Systemd 等进程管理工具。  
- 根据需要将静态资源托管至 CDN。  

### Docker 化

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV APP_PORT=8888
EXPOSE 8888

CMD ["python", "-m", "tornado_starter"]
```

## 许可证

MIT License

## 贡献

欢迎通过 Issue 或 Pull Request 提交建议或改进！

