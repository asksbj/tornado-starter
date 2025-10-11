#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
请求处理器模块
"""

import json
import tornado.web
from datetime import datetime


class BaseHandler(tornado.web.RequestHandler):
    """基础处理器类"""
    
    def set_default_headers(self):
        """设置默认响应头"""
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    
    def write_json(self, data, status_code=200):
        """返回JSON响应"""
        self.set_status(status_code)
        self.write(json.dumps(data, ensure_ascii=False, indent=2))
    
    def get_current_user(self):
        """获取当前用户（可扩展）"""
        return self.get_secure_cookie("user")


class MainHandler(tornado.web.RequestHandler):
    """主页处理器"""
    
    def get(self):
        """处理GET请求"""
        self.render("index.html", 
                   title="Tornado Web应用", 
                   message="欢迎使用Tornado框架！",
                   current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class ApiHandler(BaseHandler):
    """API处理器"""
    
    def get(self, endpoint):
        """处理API GET请求"""
        if endpoint == "info":
            self.write_json({
                "message": "Tornado API服务运行正常",
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0"
            })
        elif endpoint == "status":
            self.write_json({
                "status": "ok",
                "uptime": "运行中"
            })
        else:
            self.write_json({
                "error": f"未知的API端点: {endpoint}"
            }, 404)
    
    def post(self, endpoint):
        """处理API POST请求"""
        if endpoint == "echo":
            try:
                data = json.loads(self.request.body)
                self.write_json({
                    "message": "收到数据",
                    "data": data,
                    "timestamp": datetime.now().isoformat()
                })
            except json.JSONDecodeError:
                self.write_json({
                    "error": "无效的JSON数据"
                }, 400)
        else:
            self.write_json({
                "error": f"未知的API端点: {endpoint}"
            }, 404)
    
    def options(self, endpoint):
        """处理OPTIONS请求（CORS预检）"""
        self.set_status(204)
        self.finish()

