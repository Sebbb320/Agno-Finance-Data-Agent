# ChatGPT 4.1 Nano 集成指南

## 概述

本文档说明如何在Agno项目中集成和使用ChatGPT 4.1 nano模型。

## 已完成的配置

### 1. 设置文件更新

已更新以下设置文件以支持ChatGPT 4.1 nano：

- `agents/settings.py` - 添加了 `gpt_4_1_nano` 配置
- `teams/settings.py` - 添加了 `gpt_4_1_nano` 配置  
- `workflows/settings.py` - 添加了 `gpt_4_1_nano` 配置

### 2. UI界面更新

- `ui/utils.py` - 在模型选择器中添加了 "gpt-4.1-nano" 选项
- `ui/Home.py` - 添加了Nano Sage的入口按钮
- `ui/pages/4_Nano_Sage.py` - 创建了专门的Nano Sage页面

### 3. 新的Agent

- `agents/nano_sage.py` - 创建了专门使用ChatGPT 4.1 nano的Nano Sage Agent
- `agents/finance_agent.py` - 更新了Finance Agent以支持ChatGPT 4.1 nano

## 使用方法

### 1. 启动应用

```bash
# 激活虚拟环境
source venv/bin/activate

# 启动应用
streamlit run ui/Home.py
```

### 2. 访问支持ChatGPT 4.1 nano的Agent

1. 打开浏览器访问 `http://localhost:8501`
2. 在主页选择以下任一Agent：
   - 点击 "Launch Nano Sage" 按钮
   - 点击 "Launch Finance Agent" 按钮
3. 在侧边栏选择 "gpt-4.1-nano" 模型
4. 开始对话

### 3. 模型选择

在UI侧边栏的模型选择器中，你可以选择：
- `gpt-4o` - 标准GPT-4模型
- `gpt-4o-mini` - 轻量级GPT-4模型
- `gpt-4.1-nano` - ChatGPT 4.1 nano (使用gpt-4o-mini作为等效模型)
- `o3-mini` - 其他轻量级模型

## 技术实现

### 模型映射

由于ChatGPT 4.1 nano是较新的模型，我们暂时使用 `gpt-4o-mini` 作为等效模型：

```python
gpt_4_1_nano: str = "gpt-4o-mini"  # ChatGPT 4.1 nano (using gpt-4o-mini as equivalent)
```

### Agent配置

支持ChatGPT 4.1 nano的Agent专门优化了以下特性：
- 快速响应时间
- 成本效益处理
- 清晰简洁的沟通
- 网络搜索能力
- 实用和可操作的建议

**Nano Sage Agent**: 轻量级通用助手，适合快速问答
**Finance Agent**: 金融数据分析专家，支持股票分析、市场新闻、数据可视化、文件上传分析

## 自定义配置

### 修改模型设置

如果你想使用不同的模型作为ChatGPT 4.1 nano的等效模型，可以修改设置文件：

```python
# 在 agents/settings.py, teams/settings.py, workflows/settings.py 中
gpt_4_1_nano: str = "your-preferred-model-id"
```

### 创建自定义Agent

参考 `agents/nano_sage.py` 创建你自己的Agent：

```python
def get_custom_nano_agent(
    model_id: Optional[str] = None,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
    model_id = model_id or agent_settings.gpt_4_1_nano
    
    return Agent(
        name="Your Custom Agent",
        agent_id="your-custom-agent",
        model=OpenAIChat(
            id=model_id,
            max_completion_tokens=agent_settings.default_max_completion_tokens,
            temperature=agent_settings.default_temperature,
        ),
        # 其他配置...
    )
```

## Finance Agent 文件上传功能

Finance Agent 现在支持文件上传功能，可以分析多种格式的数据文件：

### 支持的文件类型
- **CSV文件** (.csv) - 股票数据、财务数据、市场数据
- **Excel文件** (.xlsx) - 财务报表、分析数据、投资组合
- **PDF文件** (.pdf) - 财务报告、研究文档、市场分析
- **文本文件** (.txt) - 数据日志、分析笔记、配置信息

### 使用方法
1. 访问 Finance Agent 页面
2. 在侧边栏找到 "Add a Document" 文件上传区域
3. 上传你的数据文件
4. 询问分析需求，例如：
   - "分析这个CSV文件中的股票数据"
   - "基于上传的Excel文件生成可视化图表"
   - "提取PDF报告中的关键财务指标"

### 分析能力
- **数据清洗**: 自动处理缺失值、异常值
- **统计分析**: 描述性统计、相关性分析
- **可视化**: 生成交互式图表
- **趋势分析**: 时间序列分析
- **投资分析**: 风险评估、收益分析

## 注意事项

1. **模型可用性**: 确保你的OpenAI API密钥支持所选择的模型
2. **成本控制**: ChatGPT 4.1 nano设计为成本效益模型，适合频繁使用
3. **性能优化**: 该模型针对快速响应进行了优化
4. **功能限制**: 某些高级功能可能在轻量级模型中不可用
5. **文件大小**: 建议上传文件不超过10MB
6. **数据隐私**: 上传的文件仅用于当前会话分析

## 故障排除

### 常见问题

1. **模型不可用错误**
   - 检查OpenAI API密钥是否有效
   - 确认API密钥有足够的配额
   - 验证模型ID是否正确

2. **响应缓慢**
   - 检查网络连接
   - 确认API服务状态
   - 考虑使用更轻量级的模型

3. **功能缺失**
   - 某些高级功能可能需要完整版GPT-4
   - 检查工具配置是否正确

## 更新日志

- **v1.0**: 初始集成ChatGPT 4.1 nano支持
- 添加了Nano Sage Agent
- 更新了UI界面
- 配置了模型选择器

## 贡献

欢迎提交问题和改进建议！ 