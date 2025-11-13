#!/bin/bash

# Tornado应用启动脚本

echo "🚀 启动Tornado Web应用..."

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3，请先安装Python"
    exit 1
fi

# 检查依赖
if [ ! -f "requirements.txt" ]; then
    echo "❌ 错误: 未找到requirements.txt文件"
    exit 1
fi

# 创建虚拟环境（如果不存在）
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📥 安装依赖包..."
pip install -r requirements.txt

# 创建.env文件（如果不存在）
if [ ! -f ".env" ]; then
    echo "⚙️ 创建环境配置文件..."
    cp .env.example .env
fi

# 启动应用
echo "🌟 启动Tornado服务器..."
python -m tornado_starter

