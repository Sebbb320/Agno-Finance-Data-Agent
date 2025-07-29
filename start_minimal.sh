#!/bin/bash

echo "Starting minimal test app..."
echo "PORT: $PORT"

# 确保PORT变量被正确设置
PORT=${PORT:-8501}
echo "Using port: $PORT"

exec streamlit run minimal_test.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true 