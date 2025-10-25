"""
CarbonTrack AI Agent - LangChain Agent Orchestration
"""
from typing import Any, Dict, List
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import BaseTool
from langchain_community.chat_models import ChatOllama

from config import settings
import logging

logger = logging.getLogger(__name__)


class CarbonTrackAgent:
    """
    Main LangChain agent that orchestrates post generation, video creation,
    and LinkedIn posting for project promotion.
    """
    
    def __init__(self, tools: List[BaseTool]):
        """
        Initialize the CarbonTrack agent.
        
        Args:
            tools: List of LangChain tools (generate_post, create_video, post_to_linkedin)
        """
        self.tools = tools
        self.llm = self._initialize_llm()
        self.agent = self._create_agent()
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5
        )
        
    def _initialize_llm(self):
        """Initialize the LLM based on configuration."""
        if settings.llm_provider == "ollama":
            logger.info(f"Using Ollama with model: {settings.ollama_model}")
            return ChatOllama(
                base_url=settings.ollama_base_url,
                model=settings.ollama_model,
                temperature=0.7,
            )
        elif settings.llm_provider == "grok":
            logger.info("Using Grok/xAI")
            # Grok uses OpenAI-compatible API
            from langchain_openai import ChatOpenAI
            return ChatOpenAI(
                api_key=settings.grok_api_key,
                base_url="https://api.x.ai/v1",
                model=settings.grok_model,
                temperature=0.7,
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
    
    def _create_agent(self):
        """Create the LangChain structured chat agent."""
        # Define the agent prompt
        system_message = """You are CarbonTrack Promoter, an AI agent specialized in promoting projects on LinkedIn.

Your capabilities:
1. Generate engaging LinkedIn posts about projects
2. Create demo videos of websites
3. Post content to LinkedIn

When given a project to promote, you should:
1. First, generate a compelling LinkedIn post using the generate_post tool
2. Then, create a demo video of the project website using the create_video tool
3. Finally, post both the text and video to LinkedIn using the post_to_linkedin tool

Be professional, engaging, and highlight the key value propositions of projects.
Always confirm actions before posting to LinkedIn unless auto_post is enabled.
"""

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        return create_structured_chat_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )
    
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the agent with the given input.
        
        Args:
            input_data: Dictionary containing project information:
                - website_url: URL of the project website
                - project_name: Name of the project
                - description: Project description
                - key_features: List of key features
                - tone: Optional post tone override
        
        Returns:
            Dictionary with results from each step
        """
        logger.info(f"Starting CarbonTrack agent for project: {input_data.get('project_name')}")
        
        # Format the input for the agent
        formatted_input = self._format_input(input_data)
        
        try:
            result = self.agent_executor.invoke({
                "input": formatted_input
            })
            logger.info("Agent execution completed successfully")
            return result
        except Exception as e:
            logger.error(f"Agent execution failed: {e}")
            raise
    
    def _format_input(self, input_data: Dict[str, Any]) -> str:
        """Format the input data into a prompt for the agent."""
        project_name = input_data.get("project_name", "Unknown Project")
        website_url = input_data.get("website_url", "")
        description = input_data.get("description", "")
        key_features = input_data.get("key_features", [])
        tone = input_data.get("tone", settings.default_post_tone)
        
        features_str = "\n".join(f"- {feature}" for feature in key_features)
        
        prompt = f"""
Please promote the following project on LinkedIn:

Project: {project_name}
Website: {website_url}
Description: {description}

Key Features:
{features_str}

Tone: {tone}

Steps to complete:
1. Generate a {tone} LinkedIn post about this project
2. Create a {settings.video_duration}-second demo video of the website
3. {"Automatically post" if settings.auto_post else "Prepare to post"} the content to LinkedIn

Please proceed with these steps.
"""
        return prompt.strip()
    
    async def arun(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Async version of run method.
        
        Args:
            input_data: Same as run()
        
        Returns:
            Same as run()
        """
        # For now, just call the sync version
        # Can be enhanced with proper async support later
        return self.run(input_data)


def create_carbontrack_agent(tools: List[BaseTool]) -> CarbonTrackAgent:
    """
    Factory function to create a CarbonTrack agent.
    
    Args:
        tools: List of LangChain tools
    
    Returns:
        Initialized CarbonTrack agent
    """
    return CarbonTrackAgent(tools)
