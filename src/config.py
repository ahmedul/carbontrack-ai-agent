"""
CarbonTrack AI Agent - Configuration Management
"""
from pathlib import Path
from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # LLM Configuration
    llm_provider: Literal["ollama", "grok"] = Field(
        default="ollama",
        description="LLM provider to use"
    )
    ollama_base_url: str = Field(
        default="http://localhost:11434",
        description="Ollama API base URL"
    )
    ollama_model: str = Field(
        default="llama2",
        description="Ollama model name"
    )
    grok_api_key: str = Field(
        default="",
        description="Grok API key from xAI"
    )
    grok_model: str = Field(
        default="grok-beta",
        description="Grok model version"
    )
    
    # LinkedIn Configuration
    linkedin_access_token: str = Field(
        default="",
        description="LinkedIn OAuth access token"
    )
    linkedin_person_urn: str = Field(
        default="urn:li:person:your_urn_here",
        description="LinkedIn Person URN (urn:li:person:xxxxx)"
    )
    linkedin_user_id: str = Field(
        default="",
        description="LinkedIn user ID (alternative to person URN)"
    )
    linkedin_email: str = Field(
        default="",
        description="LinkedIn email (for unofficial API)"
    )
    linkedin_password: str = Field(
        default="",
        description="LinkedIn password (for unofficial API)"
    )
    
    # CarbonTrack Configuration
    carbontrack_url: str = Field(
        default="https://your-carbontrack-website.com",
        description="URL of the CarbonTrack website for demo videos"
    )
    
    # Video Settings
    video_duration: int = Field(
        default=30,
        description="Video duration in seconds"
    )
    video_resolution: str = Field(
        default="1920x1080",
        description="Video resolution (WIDTHxHEIGHT)"
    )
    video_fps: int = Field(
        default=30,
        description="Video frames per second"
    )
    video_format: str = Field(
        default="mp4",
        description="Video output format"
    )
    
    # Agent Behavior
    default_post_tone: Literal["professional", "casual", "enthusiastic", "technical"] = Field(
        default="professional",
        description="Default tone for generated posts"
    )
    auto_post: bool = Field(
        default=False,
        description="Automatically post to LinkedIn without confirmation"
    )
    max_post_length: int = Field(
        default=2000,
        description="Maximum character length for posts"
    )
    
    # Logging
    log_level: str = Field(
        default="INFO",
        description="Logging level"
    )
    log_file: str = Field(
        default="carbontrack.log",
        description="Log file path"
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()


# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
TOOLS_DIR = SRC_DIR / "tools"
EXAMPLES_DIR = PROJECT_ROOT / "examples"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)


# Post generation templates
POST_TEMPLATES = {
    "professional": """
    Create a professional LinkedIn post about {project_name}.
    
    Project Description: {description}
    Key Features: {features}
    Website: {website_url}
    
    The post should:
    - Be engaging and informative
    - Highlight the key value proposition
    - Include relevant hashtags
    - Be under {max_length} characters
    - Have a professional tone
    - Include a call-to-action
    """,
    
    "casual": """
    Write a friendly, casual LinkedIn post about {project_name}.
    
    What it does: {description}
    Cool features: {features}
    Check it out: {website_url}
    
    Make it:
    - Conversational and approachable
    - Exciting but not overhyped
    - Easy to read
    - Under {max_length} characters
    - Include emojis where appropriate
    - End with an invitation to try it
    """,
    
    "enthusiastic": """
    Create an enthusiastic LinkedIn post announcing {project_name}!
    
    What makes it amazing: {description}
    Standout features: {features}
    Link: {website_url}
    
    Make it:
    - Exciting and energetic
    - Show genuine passion
    - Inspire curiosity
    - Under {max_length} characters
    - Use powerful language
    - Create FOMO (fear of missing out)
    """,
    
    "technical": """
    Write a technical LinkedIn post about {project_name}.
    
    Technical overview: {description}
    Key capabilities: {features}
    Project link: {website_url}
    
    The post should:
    - Focus on technical details
    - Mention architecture or tech stack if relevant
    - Appeal to developers and technical professionals
    - Be under {max_length} characters
    - Include relevant technical hashtags
    - Invite technical feedback
    """
}


def get_post_template(tone: str = None) -> str:
    """Get the post generation template for a specific tone."""
    tone = tone or settings.default_post_tone
    return POST_TEMPLATES.get(tone, POST_TEMPLATES["professional"])


def get_video_dimensions() -> tuple[int, int]:
    """Parse video resolution string into width and height."""
    try:
        width, height = settings.video_resolution.split("x")
        return int(width), int(height)
    except (ValueError, AttributeError):
        return 1920, 1080  # Default
