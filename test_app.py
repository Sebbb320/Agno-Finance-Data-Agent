#!/usr/bin/env python3
"""
简单的测试应用，用于验证Railway部署
"""

import os
import streamlit as st

def main():
    st.set_page_config(
        page_title="Agno Test App",
        page_icon=":test_tube:",
        layout="wide",
    )
    
    st.title("🚀 Agno 测试应用")
    st.write("这是一个测试页面，用于验证Railway部署是否成功。")
    
    # 显示环境变量
    st.subheader("📋 环境变量检查")
    openai_key = os.getenv("OPENAI_API_KEY")
    port = os.getenv("PORT", "未设置")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**PORT:** {port}")
        st.write(f"**OPENAI_API_KEY:** {'✅ 已设置' if openai_key else '❌ 未设置'}")
    
    with col2:
        st.write(f"**PYTHONPATH:** {os.getenv('PYTHONPATH', '未设置')}")
        st.write(f"**RUNTIME_ENV:** {os.getenv('RUNTIME_ENV', '未设置')}")
    
    # 测试基本功能
    st.subheader("🧪 功能测试")
    
    if st.button("测试按钮"):
        st.success("✅ 按钮功能正常！")
    
    # 简单的输入测试
    user_input = st.text_input("输入测试", "Hello World")
    st.write(f"您输入了: {user_input}")
    
    st.subheader("🎉 部署成功！")
    st.write("如果您能看到这个页面，说明Railway部署已经成功！")
    
    # 显示系统信息
    st.subheader("💻 系统信息")
    import sys
    st.write(f"**Python版本:** {sys.version}")
    st.write(f"**Streamlit版本:** {st.__version__}")

if __name__ == "__main__":
    main() 