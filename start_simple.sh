#!/bin/bash

echo "=== Starting Simple App ==="
echo "PORT: $PORT"
echo "PWD: $(pwd)"
echo "Files:"
ls -la

# 确保PORT变量被正确设置
PORT=${PORT:-8501}
echo "Using port: $PORT"

# 启动应用，添加更多调试信息
echo "Starting streamlit..."

# 设置环境变量
export RUNTIME_ENV=production
export PYTHONPATH=/app

# 启动应用
exec streamlit run ui/Home.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false \
    --logger.level=info 