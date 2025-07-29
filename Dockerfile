FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements-minimal.txt requirements.txt

# 安装Python依赖
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt || (echo "❌ 依赖安装失败" && exit 1)

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8501

# 设置环境变量
ENV PYTHONPATH=/app

# 复制启动脚本
COPY start.sh .
COPY start_test.sh .
COPY start_minimal.sh .
RUN chmod +x start.sh start_test.sh start_minimal.sh

# 启动命令（使用最简单的测试版本）
CMD ["./start_minimal.sh"]
