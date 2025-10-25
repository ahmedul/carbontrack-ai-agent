"""
CarbonTrack AI Agent

An open-source AI agent for automating LinkedIn promotion of projects.
"""

__version__ = "0.1.0"
__author__ = "Ahmed Ul Kabir"
__license__ = "MIT"

from .config import settings
from .agent import create_carbontrack_agent, CarbonTrackAgent
from .tools import GeneratePostTool, CreateVideoTool, PostToLinkedInTool

__all__ = [
    "settings",
    "create_carbontrack_agent",
    "CarbonTrackAgent",
    "GeneratePostTool",
    "CreateVideoTool",
    "PostToLinkedInTool",
]
