#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
应用启动脚本
"""

import os
import sys
from app import main

if __name__ == "__main__":
    # 设置环境变量
    if not os.getenv('APP_PORT'):
        os.environ['APP_PORT'] = '8888'
    if not os.getenv('APP_DEBUG'):
        os.environ['APP_DEBUG'] = 'True'
    
    # 启动应用
    main()

