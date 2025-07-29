#!/bin/bash

# Railway测试启动脚本
set -e

echo "🧪 启动测试应用..."

# 检查Python环境
echo "🐍 检查Python环境..."
python --version

# 检查环境变量
echo "🔧 检查环境变量..."
echo "PORT: ${PORT:-未设置}"
echo "OPENAI_API_KEY: ${OPENAI_API_KEY:+已设置}"

# 设置环境变量
export STREAMLIT_SERVER_PORT=${PORT:-8501}
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export PYTHONPATH=/app

echo "📊 应用配置:"
echo "  - 端口: $STREAMLIT_SERVER_PORT"
echo "  - 地址: $STREAMLIT_SERVER_ADDRESS"

# 启动测试应用
echo "🚀 启动测试应用..."
exec streamlit run test_app.py \
    --server.port=$STREAMLIT_SERVER_PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --browser.gatherUsageStats=false 