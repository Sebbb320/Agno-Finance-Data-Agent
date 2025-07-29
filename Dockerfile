FROM python:3.11-slim

WORKDIR /app

# 安装依赖
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements-core.txt

# 复制应用文件
COPY . .
COPY start_simple.sh .

# 设置权限
RUN chmod +x start_simple.sh

# 暴露端口
EXPOSE 8501

# 启动命令
CMD ["./start_simple.sh"]
