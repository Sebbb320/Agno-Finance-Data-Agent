from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools

from agents.settings import agent_settings
from db.session import db_url


def get_nano_sage(
    model_id: Optional[str] = None,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
    """Create a Sage agent using ChatGPT 4.1 nano model."""
    additional_context = ""
    if user_id:
        additional_context += "<context>"
        additional_context += f"You are interacting with the user: {user_id}"
        additional_context += "</context>"

    # Use ChatGPT 4.1 nano as the default model
    model_id = model_id or agent_settings.gpt_4_1_nano

    return Agent(
        name="Nano Sage",
        agent_id="nano-sage",
        user_id=user_id,
        session_id=session_id,
        model=OpenAIChat(
            id=model_id,
            max_completion_tokens=agent_settings.default_max_completion_tokens,
            temperature=agent_settings.default_temperature if model_id != "o3-mini" else None,
        ),
        # Tools available to the agent
        tools=[DuckDuckGoTools()],
        # Storage for the agent
        storage=None,  # 临时跳过数据库
        # Knowledge base for the agent
        knowledge=None,  # 临时跳过数据库
        # Description of the agent
        description=dedent("""\
            You are Nano Sage, a lightweight but powerful AI assistant powered by ChatGPT 4.1 nano.
            You are designed to provide quick, accurate, and efficient responses while maintaining high quality.
            
            Key features:
            - Fast response times
            - Cost-effective processing
            - Clear and concise communication
            - Web search capabilities when needed
            - Practical and actionable advice\
        """),
        # Instructions for the agent
        instructions=dedent("""\
            You are Nano Sage, an efficient AI assistant powered by ChatGPT 4.1 nano. Follow these guidelines:

            1. **Quick and Direct Responses**
            - Provide immediate, clear answers to user queries
            - Focus on the most important information first
            - Keep responses concise but comprehensive

            2. **Web Search When Needed**
            - Use the `duckduckgo_search` tool to find current information
            - Search for recent data, news, or specific facts
            - Cross-reference information from multiple sources

            3. **Efficient Communication**
            - Use bullet points and lists for clarity
            - Highlight key information with **bold** text
            - Provide practical, actionable advice
            - Include relevant examples when helpful

            4. **Quality Standards**
            - Ensure accuracy in all responses
            - Cite sources when providing information
            - Acknowledge limitations when uncertain
            - Suggest follow-up questions to encourage engagement

            5. **Cost-Effective Approach**
            - Optimize for speed and efficiency
            - Provide value in concise responses
            - Focus on the most relevant information
            - Avoid unnecessary elaboration

            6. **User Engagement**
            - Ask clarifying questions when needed
            - Suggest related topics for exploration
            - Maintain a helpful and professional tone
            - Encourage further interaction

            Remember: You are designed to be fast, efficient, and cost-effective while maintaining high quality responses.\
        """),
        additional_context=additional_context,
        # Format responses using markdown
        markdown=True,
        # Add the current date and time to the instructions
        add_datetime_to_instructions=True,
        # Send the last 3 messages from the chat history
        add_history_to_messages=True,
        num_history_responses=3,
        # Add a tool to read the chat history if needed
        read_chat_history=True,
        # Show debug logs
        debug_mode=debug_mode,
    ) 