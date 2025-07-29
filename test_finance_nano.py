#!/usr/bin/env python3
"""
测试Finance Agent使用ChatGPT 4.1 nano的功能
"""

import asyncio
from agents.finance_agent import get_finance_agent
from agents.settings import agent_settings

async def test_finance_nano():
    """测试Finance Agent使用ChatGPT 4.1 nano"""
    
    print("🧪 测试Finance Agent使用ChatGPT 4.1 nano...")
    
    # 创建使用ChatGPT 4.1 nano的Finance Agent
    finance_agent = get_finance_agent(
        model_id=agent_settings.gpt_4_1_nano,
        user_id="test_user",
        session_id="test_session"
    )
    
    print(f"✅ Finance Agent创建成功")
    print(f"📊 使用的模型: {finance_agent.model.id}")
    print(f"🔧 可用工具: {[tool.name for tool in finance_agent.tools]}")
    
    # 测试简单查询
    test_query = "分析AAPL股票的基本信息"
    print(f"\n💬 测试查询: {test_query}")
    
    try:
        response = await finance_agent.arun(test_query)
        print(f"✅ 响应成功: {str(response)[:100]}...")
    except Exception as e:
        print(f"❌ 响应失败: {str(e)}")
    
    print("\n🎉 Finance Agent ChatGPT 4.1 nano测试完成!")

if __name__ == "__main__":
    asyncio.run(test_finance_nano()) 