from pydantic_settings import BaseSettings


class AgentSettings(BaseSettings):
    """Agent settings that can be set using environment variables.
    Reference: https://pydantic-docs.helpmanual.io/usage/settings/
    """

    gpt_4_mini: str = "gpt-4o-mini"
    gpt_4: str = "gpt-4o"
    gpt_4_1_nano: str = "gpt-4o-mini"  # ChatGPT 4.1 nano (using gpt-4o-mini as equivalent)
    embedding_model: str = "text-embedding-3-small"
    default_max_completion_tokens: int = 16000
    default_temperature: float = 0.7
    # 添加超时设置
    default_timeout: int = 60  # 60秒超时
    default_connect_timeout: int = 30  # 连接超时30秒
    default_read_timeout: int = 60  # 读取超时60秒


# Create an TeamSettings object
agent_settings = AgentSettings()
