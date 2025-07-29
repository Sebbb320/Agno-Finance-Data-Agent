#!/usr/bin/env python3
"""
测试Finance Agent的文件上传功能
"""

import os
import pandas as pd
from dotenv import load_dotenv

def create_test_csv():
    """创建测试用的CSV文件"""
    # 创建示例股票数据
    data = {
        'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'Stock': ['AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL'],
        'Open': [150.0, 151.2, 149.8, 152.5, 153.1],
        'High': [152.5, 153.8, 151.5, 154.2, 155.0],
        'Low': [149.5, 150.8, 148.9, 151.8, 152.5],
        'Close': [151.2, 149.8, 152.5, 153.1, 154.8],
        'Volume': [1000000, 1200000, 950000, 1100000, 1300000]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('test_stock_data.csv', index=False)
    print("✅ 创建测试CSV文件: test_stock_data.csv")
    return 'test_stock_data.csv'

def create_test_excel():
    """创建测试用的Excel文件"""
    # 创建示例财务数据
    data = {
        'Company': ['Apple', 'Google', 'Microsoft', 'Amazon', 'Tesla'],
        'Revenue': [394328, 307394, 198270, 514000, 96773],
        'Profit': [96995, 76033, 72461, 21320, 15023],
        'Market_Cap': [3000000, 2000000, 2500000, 1800000, 800000],
        'P/E_Ratio': [31.2, 28.5, 35.1, 85.2, 45.8]
    }
    
    df = pd.DataFrame(data)
    df.to_excel('test_financial_data.xlsx', index=False)
    print("✅ 创建测试Excel文件: test_financial_data.xlsx")
    return 'test_financial_data.xlsx'

def test_finance_agent():
    """测试Finance Agent"""
    print("🧪 测试Finance Agent文件上传功能...")
    
    # 加载环境变量
    load_dotenv()
    
    try:
        # 导入Finance Agent
        from agents.finance_agent import get_finance_agent
        
        # 创建Finance Agent
        agent = get_finance_agent(user_id="test_user", model_id="gpt-4o-mini")
        print("✅ Finance Agent创建成功")
        
        # 检查knowledge功能
        if agent.knowledge:
            print("✅ Knowledge功能已启用")
        else:
            print("❌ Knowledge功能未启用")
            return False
        
        # 检查工具
        tools = [tool.name for tool in agent.tools]
        print(f"✅ 可用工具: {tools}")
        
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

def main():
    """主函数"""
    print("🚀 开始测试Finance Agent文件上传功能...\n")
    
    # 创建测试文件
    csv_file = create_test_csv()
    excel_file = create_test_excel()
    
    # 测试Finance Agent
    success = test_finance_agent()
    
    print("\n" + "="*50)
    if success:
        print("🎉 Finance Agent文件上传功能测试成功！")
        print("✅ 可以上传以下文件类型:")
        print("   - CSV文件 (.csv) - 股票数据、财务数据")
        print("   - Excel文件 (.xlsx) - 财务报表、分析数据")
        print("   - PDF文件 (.pdf) - 财务报告、研究文档")
        print("   - 文本文件 (.txt) - 数据日志、分析笔记")
        print("\n💡 使用方法:")
        print("   1. 启动应用: streamlit run ui/Home.py")
        print("   2. 访问Finance Agent页面")
        print("   3. 在侧边栏上传文件")
        print("   4. 询问分析需求")
    else:
        print("❌ Finance Agent文件上传功能测试失败")
    
    print("="*50)

if __name__ == "__main__":
    main() 