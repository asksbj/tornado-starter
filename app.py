#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tornado Web应用主文件
"""

import os
import sys
import tornado.ioloop
import tornado.web
import tornado.options
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from handlers import MainHandler, ApiHandler
from settings import settings


class Application(tornado.web.Application):
    """Tornado应用主类"""
    
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/api/(.*)", ApiHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
        ]
        
        super().__init__(handlers, **settings)


def make_app():
    """创建应用实例"""
    return Application()


def main():
    """主函数"""
    # 解析命令行参数
    tornado.options.parse_command_line()
    
    # 创建应用
    app = make_app()
    
    # 获取端口号
    port = int(os.getenv('APP_PORT', 8888))
    
    print(f"启动Tornado服务器在端口 {port}")
    print(f"访问地址: http://localhost:{port}")
    
    # 启动服务器
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

