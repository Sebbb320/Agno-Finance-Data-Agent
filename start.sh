#!/bin/bash

# Railway部署启动脚本
set -e  # 遇到错误时退出

echo "🚀 启动Agno应用..."

# 检查Python环境
echo "🐍 检查Python环境..."
python --version
pip list | head -10

# 检查环境变量
echo "🔧 检查环境变量..."
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  警告: OPENAI_API_KEY未设置，某些功能可能无法正常工作"
else
    echo "✅ OPENAI_API_KEY已设置"
fi

# 检查数据库配置
if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_DATABASE" ]; then
    echo "⚠️  警告: 数据库配置不完整，将使用内存存储模式"
    echo "💡 提示: 如需持久化存储，请配置数据库环境变量"
else
    echo "✅ 数据库配置已设置"
fi

# 设置环境变量
export PYTHONPATH=/app

echo "📊 应用配置:"
echo "  - 端口: ${PORT:-8501}"
echo "  - PYTHONPATH: $PYTHONPATH"

# 检查应用文件
echo "📁 检查应用文件..."
ls -la ui/
ls -la ui/Home.py

# 启动Streamlit应用
echo "🚀 启动Streamlit应用..."
# 确保端口变量被正确设置
PORT=${PORT:-8501}
echo "Using port: $PORT"

exec streamlit run ui/Home.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --browser.gatherUsageStats=false \
    --logger.level=info 