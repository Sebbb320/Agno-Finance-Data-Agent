FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements-railway.txt requirements.txt

# 安装Python依赖
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt || (echo "❌ 依赖安装失败" && exit 1)

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8501

# 设置环境变量
ENV PYTHONPATH=/app
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# 复制启动脚本
COPY start.sh .
COPY start_test.sh .
RUN chmod +x start.sh start_test.sh

# 启动命令（可以选择测试模式或正常模式）
CMD ["./start.sh"]
