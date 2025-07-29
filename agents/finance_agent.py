from typing import Optional
from textwrap import dedent

# 临时自定义 Tool 基类，兼容 agno.tools.base 不存在的情况
class Tool:
    name = ""
    description = ""
    def run(self, *args, **kwargs):
        raise NotImplementedError

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
# 暂时注释掉knowledge功能，因为当前Agno版本不支持
# from agno.agent import AgentKnowledge
# from agno.storage.knowledge.postgres import PostgresKnowledgeStorage
# from db.session import db_url

# 新增 PandasTools
class PandasTools(Tool):
    name = "pandas_tools"
    description = "数据清洗、分组、聚合、统计分析等"

    def run(self, data, operation, **kwargs):
        import pandas as pd
        df = pd.DataFrame(data)
        if operation == "describe":
            return df.describe().to_dict()
        elif operation == "groupby":
            group_col = kwargs.get("group_col")
            agg_col = kwargs.get("agg_col")
            return df.groupby(group_col)[agg_col].sum().to_dict()
        # 可扩展更多操作
        return {"error": "Unsupported operation"}

# 新增 AltairTools
class AltairTools(Tool):
    name = "altair_tools"
    description = "数据可视化工具，支持生成常见图表（如折线图、柱状图、饼图等）"

    def run(self, data, chart_type="line", x=None, y=None, color=None, **kwargs):
        import pandas as pd
        import altair as alt
        df = pd.DataFrame(data)
        if chart_type == "line":
            chart = alt.Chart(df).mark_line().encode(x=x, y=y, color=color)
        elif chart_type == "bar":
            chart = alt.Chart(df).mark_bar().encode(x=x, y=y, color=color)
        elif chart_type == "area":
            chart = alt.Chart(df).mark_area().encode(x=x, y=y, color=color)
        elif chart_type == "point":
            chart = alt.Chart(df).mark_point().encode(x=x, y=y, color=color)
        else:
            return {"error": "Unsupported chart type"}
        return chart.to_dict()  # 返回 Altair 图表的 JSON 结构，供前端渲染


def get_finance_agent(
    model_id: Optional[str] = None,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
    """创建一个金融数据分析 Agent，集成 yfinance、pandas、altair 和网页搜索工具"""
    additional_context = ""
    if user_id:
        additional_context += "<context>"
        additional_context += f"You are interacting with the user: {user_id}"
        additional_context += "</context>"

    # 导入设置
    from agents.settings import agent_settings
    model_id = model_id or agent_settings.gpt_4

    return Agent(
        name="FinanceAgent",
        agent_id="finance_agent",
        user_id=user_id,
        session_id=session_id,
        model=OpenAIChat(
            id=model_id,
            max_completion_tokens=4096,
            temperature=0.2,
        ),
        tools=[
            YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
            DuckDuckGoTools(),
            PandasTools(),
            AltairTools(),  # 新增 Altair 可视化工具
        ],
        # 暂时注释掉knowledge功能
        # knowledge=AgentKnowledge(
        #     storage=PostgresKnowledgeStorage(
        #         table_name="finance_agent_knowledge",
        #         db_url=db_url,
        #     ),
        # ),
        description=dedent("""
            你是 FinanceAgent，一个专注于金融数据分析和实时信息检索的智能体。
            你可以获取股票行情、公司信息、分析师评级、相关新闻，并结合实时互联网信息进行综合分析。
            你还可以用 Pandas 工具进行数据清洗、分组、聚合和统计分析，并用 Altair 工具生成可视化图表。
            回答要结构清晰、数据充分，必要时用表格和图表展示。
        """),
        instructions=dedent("""
            1. 优先用 yfinance 工具获取股票、公司、市场等金融数据。
            2. 如需补充最新新闻或行业动态，使用 duckduckgo_search 工具。
            3. 如需对数据进一步分析、分组、统计，使用 pandas_tools。
            4. 如需生成可视化图表，使用 altair_tools。
            5. 回答要有数据支撑，适当用表格和图表展示。
            6. 结论要有来源，引用数据和新闻出处。
            7. 如有不确定，主动说明并建议用户进一步查询。
            8. 如果用户上传了文件（CSV、Excel、PDF等），优先分析这些文件中的数据。
            9. 结合上传的文件数据和在线金融数据进行综合分析。
            10. 对上传的CSV文件进行数据清洗、统计分析和可视化。
        """),
        additional_context=additional_context,
        markdown=True,
        add_datetime_to_instructions=True,
        add_history_to_messages=True,
        num_history_responses=3,
        read_chat_history=True,
        debug_mode=debug_mode,
    ) 