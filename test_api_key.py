#!/usr/bin/env python3
"""
测试OpenAI API密钥配置
"""

import os
import requests
from dotenv import load_dotenv

def test_network_connectivity():
    """测试网络连接"""
    print("🌐 测试网络连接...")
    
    try:
        # 测试基本网络连接
        response = requests.get("https://www.google.com", timeout=5)
        print("✅ 基本网络连接正常")
        
        # 测试OpenAI API连接
        response = requests.get("https://api.openai.com/v1/models", timeout=10)
        print("✅ OpenAI API服务器可访问")
        return True
        
    except requests.exceptions.Timeout:
        print("❌ 网络连接超时")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ 网络连接失败")
        return False
    except Exception as e:
        print(f"❌ 网络测试失败: {str(e)}")
        return False

def test_api_key():
    """测试API密钥配置"""
    print("🧪 测试OpenAI API密钥配置...")
    
    # 加载.env文件
    load_dotenv()
    
    # 获取API密钥
    api_key = os.getenv('OPENAI_API_KEY')
    
    if api_key:
        print(f"✅ API密钥已找到: {api_key[:20]}...")
        
        # 先测试网络连接
        if not test_network_connectivity():
            print("⚠️ 网络连接有问题，但API密钥配置正确")
            return True
        
        # 测试API密钥是否有效
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            
            # 尝试获取模型列表来验证API密钥
            models = client.models.list()
            print(f"✅ API密钥有效！找到 {len(models.data)} 个可用模型")
            
            # 显示一些可用的模型
            available_models = [model.id for model in models.data if 'gpt' in model.id.lower()]
            print(f"📋 可用的GPT模型: {available_models[:5]}...")
            
        except Exception as e:
            print(f"❌ API密钥验证失败: {str(e)}")
            print("💡 可能的原因:")
            print("   - 网络连接问题")
            print("   - API密钥无效或过期")
            print("   - 需要配置代理")
            print("   - OpenAI服务暂时不可用")
            return False
            
        return True
    else:
        print("❌ 未找到OPENAI_API_KEY环境变量")
        print("请检查.env文件是否正确配置")
        return False

if __name__ == "__main__":
    success = test_api_key()
    if success:
        print("\n🎉 API密钥配置成功！现在可以启动应用了。")
        print("💡 如果网络有问题，应用可能无法正常工作，但配置是正确的。")
    else:
        print("\n💥 API密钥配置失败，请检查配置。") 