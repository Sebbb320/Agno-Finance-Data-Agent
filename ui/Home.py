import asyncio

import nest_asyncio
import streamlit as st
from agno.tools.streamlit.components import check_password
from dotenv import load_dotenv

from ui.css import CUSTOM_CSS
from ui.utils import about_agno, footer

# 加载.env文件中的环境变量
load_dotenv()

nest_asyncio.apply()

st.set_page_config(
    page_title="Agno Agents",
    page_icon=":orange_heart:",
    layout="wide",
)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


async def header():
    st.markdown("<h1 class='heading'>Agno Agents</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='subheading'>Welcome to the Agno Agents platform! We've provided some sample agents to get you started.</p>",
        unsafe_allow_html=True,
    )


async def body():
    st.markdown("### Available Agents")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Sage</h3>
            <p>A knowledge agent that uses Agentic RAG to deliver context-rich answers from a knowledge base.</p>
            <p>Perfect for exploring your own knowledge base.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Sage", key="sage_button"):
            st.switch_page("pages/1_Sage.py")

    with col2:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Scholar</h3>
            <p>A research agent that uses DuckDuckGo to deliver in-depth answers about any topic.</p>
            <p>Perfect for exploring general knowledge from the web.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Scholar", key="scholar_button"):
            st.switch_page("pages/2_Scholar.py")

    # 新增 Nano Sage 入口
    st.markdown("### Lightweight Agents")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Nano Sage</h3>
            <p>A lightweight but powerful AI assistant powered by ChatGPT 4.1 nano.</p>
            <p>Fast, efficient, and cost-effective for quick responses.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Nano Sage", key="nano_sage_button"):
            st.switch_page("pages/4_Nano_Sage.py")

    # 新增 Finance Agent 入口
    st.markdown("### Data & Finance Agents")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Finance Agent</h3>
            <p>专注于金融数据分析、实时信息检索、Pandas数据处理和Altair可视化的智能体。</p>
            <p>支持多种模型选择，包括ChatGPT 4.1 nano，快速高效。</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Finance Agent", key="finance_agent_button"):
            st.switch_page("pages/3_Finance_Agent.py")

    st.markdown("### Available Teams")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Multi-language team</h3>
            <p>A team of agents designed to answer questions in different languages.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Multi-language team", key="multi_language_button"):
            st.switch_page("pages/3_Language_team.py")

    with col2:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Finance research team</h3>
            <p>A team of agents designed to produce financial research reports by combining market data analysis with relevant web information.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Finance team", key="finance_team_button"):
            st.switch_page("pages/4_Finance_team.py")

    st.markdown("### Available Workflows")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Blog post generator</h3>
            <p>A workflow designed to generate blog posts.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Blog post generator", key="blog_post_generator_button"):
            st.switch_page("pages/5_Blog_post_generator.py")

    with col2:
        st.markdown(
            """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;">
            <h3>Investment report generator</h3>
            <p>A workflow designed to generate investment reports.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Launch Investment report generator", key="investment_report_generator_button"):
            st.switch_page("pages/6_Investment_report_generator.py")


async def main():
    await header()
    await body()
    await footer()
    await about_agno()


if __name__ == "__main__":
    if check_password():
        asyncio.run(main())
