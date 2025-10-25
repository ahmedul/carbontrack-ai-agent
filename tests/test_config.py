"""
Tests for configuration module
"""
import pytest
from config import settings, get_post_template, get_video_dimensions


def test_settings_default_values():
    """Test that settings have sensible defaults."""
    assert settings.llm_provider in ["ollama", "grok"]
    assert settings.max_post_length > 0
    assert settings.video_duration > 0


def test_get_post_template():
    """Test post template retrieval."""
    template = get_post_template("professional")
    assert template is not None
    assert "{project_name}" in template
    assert "{website_url}" in template
    
    # Test fallback to professional
    template = get_post_template("nonexistent")
    assert template is not None


def test_get_video_dimensions():
    """Test video dimension parsing."""
    width, height = get_video_dimensions()
    assert width > 0
    assert height > 0
    assert isinstance(width, int)
    assert isinstance(height, int)


def test_post_templates_exist():
    """Test that all tone templates are available."""
    tones = ["professional", "casual", "enthusiastic", "technical"]
    for tone in tones:
        template = get_post_template(tone)
        assert template is not None
        assert len(template) > 0
