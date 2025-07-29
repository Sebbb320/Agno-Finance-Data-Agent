#!/bin/bash

# 部署脚本 - 将Agno应用部署到公网

echo "🚀 开始部署Agno应用到公网..."

# 检查环境变量
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ 错误: 请设置OPENAI_API_KEY环境变量"
    echo "export OPENAI_API_KEY=your_api_key_here"
    exit 1
fi

# 构建Docker镜像
echo "📦 构建Docker镜像..."
docker build -t agno-finance-app .

# 运行容器
echo "🏃 启动应用容器..."
docker run -d \
    --name agno-app \
    -p 8501:8501 \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    -e PYTHONPATH=/app \
    -e STREAMLIT_SERVER_PORT=8501 \
    -e STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    --restart unless-stopped \
    agno-finance-app

echo "✅ 部署完成！"
echo "🌐 应用地址: http://localhost:8501"
echo "📊 查看日志: docker logs agno-app"
echo "🛑 停止应用: docker stop agno-app" 