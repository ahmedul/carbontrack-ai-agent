"""
Generate Post Tool - Creates LinkedIn posts using LLM
"""
from typing import Any, Dict, Optional, Type
from langchain_core.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field
from langchain_community.chat_models import ChatOllama

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config import settings, get_post_template
import logging

logger = logging.getLogger(__name__)


class GeneratePostInput(BaseModel):
    """Input schema for the GeneratePost tool."""
    project_name: str = Field(description="Name of the project to promote")
    description: str = Field(description="Description of the project")
    website_url: str = Field(description="URL of the project website")
    key_features: str = Field(
        description="Comma-separated list of key features",
        default=""
    )
    tone: str = Field(
        description="Tone of the post: professional, casual, enthusiastic, or technical",
        default="professional"
    )


class GeneratePostTool(BaseTool):
    """
    LangChain tool that generates LinkedIn posts using an LLM.
    
    This tool takes project information and generates an engaging
    LinkedIn post suitable for promotion.
    """
    
    name: str = "generate_post"
    description: str = """
    Generate an engaging LinkedIn post about a project.
    Input should include project_name, description, website_url, 
    key_features (comma-separated), and optionally tone.
    Returns the generated post text.
    """
    args_schema: Type[BaseModel] = GeneratePostInput
    
    def _run(
        self,
        project_name: str,
        description: str,
        website_url: str,
        key_features: str = "",
        tone: str = "professional",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Generate a LinkedIn post."""
        logger.info(f"Generating {tone} post for project: {project_name}")
        
        try:
            # Parse key features
            features = [f.strip() for f in key_features.split(",") if f.strip()]
            features_str = "\n".join(f"- {f}" for f in features)
            
            # Get the appropriate template
            template = get_post_template(tone)
            
            # Format the prompt
            prompt = template.format(
                project_name=project_name,
                description=description,
                features=features_str,
                website_url=website_url,
                max_length=settings.max_post_length
            )
            
            # Generate post using LLM
            if settings.llm_provider == "ollama":
                llm = ChatOllama(
                    base_url=settings.ollama_base_url,
                    model=settings.ollama_model,
                    temperature=0.7,
                )
            elif settings.llm_provider == "grok":
                from langchain_openai import ChatOpenAI
                llm = ChatOpenAI(
                    api_key=settings.grok_api_key,
                    base_url="https://api.x.ai/v1",
                    model=settings.grok_model,
                    temperature=0.7,
                )
            else:
                raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
            
            response = llm.invoke(prompt)
            post_text = response.content
            
            # Ensure post is within length limit
            if len(post_text) > settings.max_post_length:
                logger.warning(f"Post too long ({len(post_text)} chars), truncating...")
                post_text = post_text[:settings.max_post_length - 3] + "..."
            
            logger.info("Post generated successfully")
            return post_text
            
        except Exception as e:
            logger.error(f"Error generating post: {e}")
            return f"Error generating post: {str(e)}"
    
    async def _arun(
        self,
        project_name: str,
        description: str,
        website_url: str,
        key_features: str = "",
        tone: str = "professional",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Async version - for now just calls sync version."""
        return self._run(
            project_name=project_name,
            description=description,
            website_url=website_url,
            key_features=key_features,
            tone=tone,
            run_manager=run_manager,
        )


# Example usage
if __name__ == "__main__":
    tool = GeneratePostTool()
    result = tool._run(
        project_name="CarbonTrack",
        description="A sustainability tracking app that helps users reduce their carbon footprint",
        website_url="https://carbontrack.example.com",
        key_features="Carbon footprint tracking, AI recommendations, Community challenges",
        tone="professional"
    )
    print(result)
