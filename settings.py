#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
应用配置文件
"""

import os

# 基础配置
DEBUG = os.getenv('APP_DEBUG', 'True').lower() == 'true'
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# 模板和静态文件配置
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')
STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')

# Tornado设置
settings = {
    'debug': DEBUG,
    'template_path': TEMPLATE_PATH,
    'static_path': STATIC_PATH,
    'cookie_secret': SECRET_KEY,
    'xsrf_cookies': True,
    'login_url': '/login',
    'autoescape': 'xhtml_escape',
}

