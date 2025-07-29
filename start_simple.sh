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
exec streamlit run diagnose_app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false \
    --logger.level=debug 