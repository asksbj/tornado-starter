# Tornado Web应用

这是一个基于Tornado框架构建的Web应用项目模板，提供了完整的项目结构和基础功能。

## 功能特性

- 🚀 基于Tornado 6.3+的高性能Web服务器
- 🎨 现代化的Bootstrap 5 UI界面
- 📱 响应式设计，支持移动端
- 🔌 RESTful API接口
- 🛡️ XSRF保护和安全的Cookie处理
- 📝 模板引擎支持
- 🎯 静态文件服务
- ⚙️ 环境变量配置
- 📊 实时API测试功能

## 项目结构

```
tornado_starter/
├── app.py              # 主应用文件
├── handlers.py         # 请求处理器
├── settings.py         # 配置文件
├── run.py             # 启动脚本
├── requirements.txt    # 依赖包列表
├── .env.example       # 环境变量示例
├── templates/         # HTML模板
│   ├── base.html      # 基础模板
│   └── index.html     # 首页模板
├── static/           # 静态文件
│   ├── css/
│   │   └── style.css  # 自定义样式
│   ├── js/
│   │   └── main.js    # JavaScript功能
│   └── images/        # 图片资源
└── README.md         # 项目说明
```

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\\Scripts\\activate   # Windows

# 安装依赖包
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，修改配置
nano .env
```

### 3. 启动应用

```bash
# 方法1: 直接运行主文件
python app.py

# 方法2: 使用启动脚本
python run.py

# 方法3: 使用Tornado命令行
python -m tornado.autoreload app.py
```

### 4. 访问应用

打开浏览器访问: http://localhost:8888

## API接口

### 获取应用信息
```http
GET /api/info
```

### 获取服务器状态
```http
GET /api/status
```

### 数据回显测试
```http
POST /api/echo
Content-Type: application/json

{
    "message": "Hello Tornado!"
}
```

## 开发说明

### 添加新的处理器

1. 在 `handlers.py` 中创建新的处理器类
2. 继承 `BaseHandler` 或 `tornado.web.RequestHandler`
3. 在 `app.py` 中添加路由配置

```python
# handlers.py
class NewHandler(BaseHandler):
    def get(self):
        self.write_json({"message": "Hello from new handler!"})

# app.py
handlers = [
    (r"/new", NewHandler),
    # ... 其他路由
]
```

### 添加新的模板

1. 在 `templates/` 目录下创建HTML文件
2. 继承 `base.html` 模板
3. 在处理器中使用 `self.render()` 方法

```python
def get(self):
    self.render("new_template.html", data="some data")
```

### 添加静态资源

将CSS、JS、图片等文件放入 `static/` 对应子目录中，即可通过 `/static/` 路径访问。

## 配置选项

通过环境变量可以配置以下选项：

- `APP_PORT`: 应用端口（默认: 8888）
- `APP_DEBUG`: 调试模式（默认: True）
- `SECRET_KEY`: Cookie密钥（生产环境必须修改）

## 部署建议

### 生产环境部署

1. 修改 `.env` 文件中的配置
2. 设置 `APP_DEBUG=False`
3. 使用强密钥替换 `SECRET_KEY`
4. 考虑使用反向代理（如Nginx）
5. 使用进程管理器（如Supervisor）

### Docker部署

可以创建 `Dockerfile` 进行容器化部署：

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8888

CMD ["python", "app.py"]
```

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个项目模板！

