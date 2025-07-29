#!/usr/bin/env python3
"""
修复网络超时问题的脚本
"""

import os
import requests
import httpx
from dotenv import load_dotenv

def fix_network_timeout():
    """修复网络超时问题"""
    print("🔧 修复网络超时问题...")
    
    # 加载环境变量
    load_dotenv()
    
    # 设置更长的超时时间
    os.environ['OPENAI_TIMEOUT'] = '60'  # 60秒超时
    os.environ['HTTPX_TIMEOUT'] = '60'
    
    print("✅ 已设置60秒超时时间")
    
    # 测试网络连接
    print("🌐 测试网络连接...")
    
    try:
        # 测试基本连接
        response = requests.get("https://api.openai.com/v1/models", 
                              timeout=30,
                              headers={"User-Agent": "Mozilla/5.0"})
        print(f"✅ OpenAI API可访问，状态码: {response.status_code}")
        
        if response.status_code == 401:
            print("⚠️ API密钥可能无效，但网络连接正常")
        elif response.status_code == 200:
            print("✅ 网络连接完全正常")
        else:
            print(f"⚠️ 服务器响应: {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("❌ 连接超时 - 可能需要代理或VPN")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ 连接错误 - 检查网络设置")
        return False
    except Exception as e:
        print(f"❌ 连接测试失败: {str(e)}")
        return False
    
    return True

def test_with_proxy():
    """测试代理设置"""
    print("🔍 测试代理设置...")
    
    # 常见的代理设置
    proxies = [
        None,  # 无代理
        {"http": "http://192.168.101.9:7890", "https": "http://192.168.101.9:7890"},  # 你的IP地址
        {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"},  # 本地代理端口
        {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"},  # SOCKS代理
    ]
    
    for i, proxy in enumerate(proxies):
        try:
            print(f"测试代理配置 {i+1}: {proxy}")
            response = requests.get("https://api.openai.com/v1/models", 
                                  timeout=10,
                                  proxies=proxy)
            print(f"✅ 代理配置 {i+1} 工作正常")
            return proxy
        except Exception as e:
            print(f"❌ 代理配置 {i+1} 失败: {str(e)}")
    
    return None

if __name__ == "__main__":
    print("🧪 开始网络诊断...\n")
    
    # 修复超时设置
    fix_network_timeout()
    
    # 测试网络连接
    if not fix_network_timeout():
        print("\n🔍 尝试代理设置...")
        working_proxy = test_with_proxy()
        
        if working_proxy:
            print(f"✅ 找到可用的代理配置: {working_proxy}")
            print("💡 请设置环境变量:")
            if working_proxy:
                print(f"export http_proxy={working_proxy['http']}")
                print(f"export https_proxy={working_proxy['https']}")
        else:
            print("❌ 所有代理配置都失败")
            print("💡 建议:")
            print("   1. 检查网络连接")
            print("   2. 尝试使用VPN")
            print("   3. 更换网络环境")
            print("   4. 检查防火墙设置")
    
    print("\n🎯 诊断完成！") 