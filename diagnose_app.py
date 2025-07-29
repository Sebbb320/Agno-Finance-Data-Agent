import streamlit as st
import os
import sys
import platform
import subprocess
import time

st.set_page_config(page_title="Railway诊断", layout="wide")

st.title("🔍 Railway 环境诊断")

# 基本系统信息
st.header("📋 系统信息")
col1, col2 = st.columns(2)

with col1:
    st.write(f"**Python版本:** {sys.version}")
    st.write(f"**平台:** {platform.platform()}")
    st.write(f"**工作目录:** {os.getcwd()}")

with col2:
    st.write(f"**Streamlit版本:** {st.__version__}")
    st.write(f"**当前时间:** {time.strftime('%Y-%m-%d %H:%M:%S')}")

# 环境变量
st.header("🔧 环境变量")
env_vars = {
    'PORT': os.getenv('PORT'),
    'RAILWAY_STATIC_URL': os.getenv('RAILWAY_STATIC_URL'),
    'RAILWAY_PUBLIC_DOMAIN': os.getenv('RAILWAY_PUBLIC_DOMAIN'),
    'RAILWAY_PROJECT_ID': os.getenv('RAILWAY_PROJECT_ID'),
    'RAILWAY_SERVICE_ID': os.getenv('RAILWAY_SERVICE_ID'),
    'NODE_ENV': os.getenv('NODE_ENV'),
    'RUNTIME_ENV': os.getenv('RUNTIME_ENV')
}

for var, value in env_vars.items():
    status = "✅" if value else "❌"
    st.write(f"{status} **{var}:** {value}")

# 文件系统
st.header("📁 文件系统")
try:
    files = os.listdir('.')
    st.write("当前目录文件:")
    for file in files:
        st.write(f"  - {file}")
except Exception as e:
    st.error(f"读取文件系统失败: {e}")

# 网络测试
st.header("🌐 网络测试")
if st.button("测试网络连接"):
    try:
        import requests
        response = requests.get('https://httpbin.org/ip', timeout=5)
        st.success(f"网络连接正常! IP: {response.json().get('origin', 'unknown')}")
    except Exception as e:
        st.error(f"网络连接失败: {e}")

# 端口测试
st.header("🔌 端口测试")
port = os.getenv('PORT', '8501')
st.write(f"当前端口: {port}")

if st.button("测试端口"):
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', int(port)))
        if result == 0:
            st.success(f"端口 {port} 可访问")
        else:
            st.error(f"端口 {port} 不可访问")
        sock.close()
    except Exception as e:
        st.error(f"端口测试失败: {e}")

# 内存信息
st.header("💾 内存信息")
try:
    import psutil
    memory = psutil.virtual_memory()
    st.write(f"**总内存:** {memory.total / 1024 / 1024:.1f} MB")
    st.write(f"**可用内存:** {memory.available / 1024 / 1024:.1f} MB")
    st.write(f"**内存使用率:** {memory.percent}%")
    
    # 进度条显示内存使用
    st.progress(memory.percent / 100)
except Exception as e:
    st.error(f"获取内存信息失败: {e}")

st.success("🎉 诊断完成！如果看到这个页面，说明应用运行正常。") 