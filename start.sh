#!/bin/bash

# Railway部署启动脚本
echo "🚀 启动Agno应用..."

# 检查环境变量
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  警告: OPENAI_API_KEY未设置，某些功能可能无法正常工作"
fi

# 检查数据库配置
if [ -z "$DB_HOST" ] || [ -z "$DB_USER" ] || [ -z "$DB_DATABASE" ]; then
    echo "⚠️  警告: 数据库配置不完整，将使用内存存储模式"
    echo "💡 提示: 如需持久化存储，请配置数据库环境变量"
fi

# 设置默认端口（Railway会自动设置$PORT）
export STREAMLIT_SERVER_PORT=${PORT:-8501}
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export PYTHONPATH=/app

echo "📊 应用将在端口 $STREAMLIT_SERVER_PORT 上运行"
echo "🌐 访问地址: http://localhost:$STREAMLIT_SERVER_PORT"

# 启动Streamlit应用
exec streamlit run ui/Home.py \
    --server.port=$STREAMLIT_SERVER_PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --browser.gatherUsageStats=false 