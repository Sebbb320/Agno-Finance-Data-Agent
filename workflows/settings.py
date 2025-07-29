from pydantic_settings import BaseSettings


class WorkflowSettings(BaseSettings):
    """Workflow settings that can be set using environment variables.

    Reference: https://pydantic-docs.helpmanual.io/usage/settings/
    """

    gpt_4_mini: str = "gpt-4o-mini"
    gpt_4_1_nano: str = "gpt-4o-mini"  # ChatGPT 4.1 nano (using gpt-4o-mini as equivalent)
    embedding_model: str = "text-embedding-3-small"
    default_max_completion_tokens: int = 16000
    default_temperature: float = 0


# Create an WorkflowSettings object
workflow_settings = WorkflowSettings()
