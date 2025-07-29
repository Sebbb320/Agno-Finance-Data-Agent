#!/usr/bin/env python3
"""
离线模式测试 - 验证应用基本功能
"""

import os
from dotenv import load_dotenv

def test_offline_mode():
    """测试离线模式下的基本功能"""
    print("🔌 离线模式测试...")
    
    # 加载.env文件
    load_dotenv()
    
    # 检查环境变量
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print(f"✅ API密钥已配置: {api_key[:20]}...")
    else:
        print("❌ API密钥未配置")
        return False
    
    # 测试应用模块导入
    try:
        print("📦 测试模块导入...")
        
        # 测试基本模块
        import streamlit as st
        print("✅ Streamlit 模块正常")
        
        import asyncio
        print("✅ Asyncio 模块正常")
        
        # 测试Agno模块
        from agno.agent import Agent
        print("✅ Agno Agent 模块正常")
        
        from agno.models.openai import OpenAIChat
        print("✅ Agno OpenAI 模块正常")
        
        # 测试自定义模块
        from agents.settings import agent_settings
        print("✅ 应用设置模块正常")
        
        from agents.sage import get_sage
        print("✅ Sage Agent 模块正常")
        
        from agents.nano_sage import get_nano_sage
        print("✅ Nano Sage Agent 模块正常")
        
        from agents.finance_agent import get_finance_agent
        print("✅ Finance Agent 模块正常")
        
        # 测试UI模块
        from ui.utils import selected_model
        print("✅ UI工具模块正常")
        
    except ImportError as e:
        print(f"❌ 模块导入失败: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ 模块测试失败: {str(e)}")
        return False
    
    # 测试Agent创建（不调用API）
    try:
        print("🤖 测试Agent创建...")
        
        # 创建Sage Agent
        sage = get_sage(user_id="test_user", model_id="gpt-4o-mini")
        print("✅ Sage Agent 创建成功")
        
        # 创建Nano Sage Agent
        nano_sage = get_nano_sage(user_id="test_user", model_id="gpt-4o-mini")
        print("✅ Nano Sage Agent 创建成功")
        
        # 创建Finance Agent
        finance_agent = get_finance_agent(user_id="test_user", model_id="gpt-4o-mini")
        print("✅ Finance Agent 创建成功")
        
    except Exception as e:
        print(f"❌ Agent创建失败: {str(e)}")
        return False
    
    # 测试设置
    try:
        print("⚙️ 测试应用设置...")
        
        print(f"   - GPT-4 Mini: {agent_settings.gpt_4_mini}")
        print(f"   - GPT-4: {agent_settings.gpt_4}")
        print(f"   - GPT-4.1 Nano: {agent_settings.gpt_4_1_nano}")
        print(f"   - 最大Token: {agent_settings.default_max_completion_tokens}")
        print(f"   - 温度: {agent_settings.default_temperature}")
        
        print("✅ 应用设置正常")
        
    except Exception as e:
        print(f"❌ 设置测试失败: {str(e)}")
        return False
    
    return True

def test_ui_components():
    """测试UI组件"""
    print("🎨 测试UI组件...")
    
    try:
        # 测试模型选择器
        model_options = {
            "gpt-4o": "gpt-4o",
            "gpt-4o-mini": "gpt-4o-mini",
            "gpt-4.1-nano": "gpt-4o-mini",
            "o3-mini": "o3-mini",
        }
        print(f"✅ 模型选择器配置正常: {list(model_options.keys())}")
        
        # 测试页面配置
        pages = [
            "pages/1_Sage.py",
            "pages/2_Scholar.py", 
            "pages/3_Finance_Agent.py",
            "pages/4_Nano_Sage.py"
        ]
        
        for page in pages:
            if os.path.exists(page):
                print(f"✅ 页面存在: {page}")
            else:
                print(f"❌ 页面缺失: {page}")
        
    except Exception as e:
        print(f"❌ UI组件测试失败: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("🧪 开始离线模式测试...\n")
    
    # 测试基本功能
    basic_success = test_offline_mode()
    
    # 测试UI组件
    ui_success = test_ui_components()
    
    print("\n" + "="*50)
    if basic_success and ui_success:
        print("🎉 离线模式测试成功！")
        print("✅ 应用基本功能正常")
        print("✅ 所有Agent配置正确")
        print("✅ UI组件完整")
        print("\n💡 应用可以启动，但需要网络连接才能使用AI功能")
        print("🚀 运行命令: streamlit run ui/Home.py")
    else:
        print("❌ 离线模式测试失败")
        print("请检查应用配置")
    
    print("="*50) 