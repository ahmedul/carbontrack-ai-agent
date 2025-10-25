"""
Tests for tools module
"""
import pytest
from unittest.mock import Mock, patch


class TestGeneratePostTool:
    """Tests for GeneratePostTool."""
    
    def test_tool_initialization(self):
        """Test that tool can be initialized."""
        from tools.generate_post import GeneratePostTool
        tool = GeneratePostTool()
        assert tool.name == "generate_post"
        assert tool.description is not None
    
    @patch('tools.generate_post.ChatOllama')
    def test_post_generation(self, mock_llm):
        """Test basic post generation."""
        from tools.generate_post import GeneratePostTool
        
        # Mock LLM response
        mock_response = Mock()
        mock_response.content = "Test post content"
        mock_llm.return_value.invoke.return_value = mock_response
        
        tool = GeneratePostTool()
        # Note: This will fail without proper setup, but shows structure
        # In real tests, we'd mock the LLM properly


class TestCreateVideoTool:
    """Tests for CreateVideoTool."""
    
    def test_tool_initialization(self):
        """Test that tool can be initialized."""
        from tools.create_video import CreateVideoTool
        tool = CreateVideoTool()
        assert tool.name == "create_video"
        assert tool.description is not None


class TestPostToLinkedInTool:
    """Tests for PostToLinkedInTool."""
    
    def test_tool_initialization(self):
        """Test that tool can be initialized."""
        from tools.post_to_linkedin import PostToLinkedInTool
        tool = PostToLinkedInTool()
        assert tool.name == "post_to_linkedin"
        assert tool.description is not None
    
    def test_preview_mode(self):
        """Test that preview mode works without credentials."""
        from tools.post_to_linkedin import PostToLinkedInTool
        tool = PostToLinkedInTool()
        result = tool._run(
            post_text="Test post",
            video_path="",
            image_path=""
        )
        assert "Preview" in result or "prepared" in result.lower()
