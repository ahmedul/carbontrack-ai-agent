# Changelog

All notable changes to the CarbonTrack Promoter AI Agent will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Multi-platform support (Twitter/X, Facebook, Instagram)
- Scheduling system for automated posting
- Analytics dashboard
- Template marketplace
- Web-based UI
- Docker containerization
- REST API mode

## [0.1.0] - 2025-10-25

### Added
- Initial release of CarbonTrack Promoter AI Agent
- LangChain-based agent orchestration
- Three core tools:
  - `generate_post`: AI-powered LinkedIn post generation
  - `create_video`: Playwright-based website demo videos
  - `post_to_linkedin`: LinkedIn API integration
- Support for multiple LLM providers:
  - Ollama (local open-source LLMs)
  - Grok/xAI (cloud-based)
- Four post tone options:
  - Professional
  - Casual
  - Enthusiastic
  - Technical
- Comprehensive configuration system using Pydantic
- Rich CLI interface with interactive mode
- Example input files for different use cases
- Automated video recording with:
  - Configurable duration
  - Custom resolution support
  - Multiple format options
- LinkedIn posting with:
  - Text posts
  - Image attachments
  - Video uploads (basic)
- Safety features:
  - Preview mode (auto-post disabled by default)
  - Environment-based configuration
  - Credential protection
- Documentation:
  - Comprehensive README
  - Quick Start Guide
  - Contributing guidelines
  - Example files
- Testing infrastructure:
  - pytest configuration
  - Basic unit tests
  - GitHub Actions CI/CD
- Open source under MIT License

### Security
- All credentials via environment variables
- No hardcoded secrets
- .gitignore configured for sensitive files
- Preview mode for content review before posting

### Developer Experience
- Type hints throughout codebase
- Rich logging with multiple levels
- Error handling and graceful failures
- Modular architecture for easy extension
- Development dependencies for testing and linting

---

## Release Notes

### Version 0.1.0 - Initial Alpha Release

This is the first public release of CarbonTrack Promoter. The agent is functional but considered alpha software. Expect:

**✅ What Works:**
- Post generation with Ollama/Grok
- Video creation from websites
- LinkedIn text posting (with preview mode)
- Multiple tone options
- CLI interface

**⚠️ Known Limitations:**
- Video posting to LinkedIn requires manual finalization
- No scheduling system yet
- Limited error recovery
- No analytics/tracking
- Single platform (LinkedIn only)

**🔜 Coming Soon:**
- Enhanced video upload to LinkedIn
- Scheduling capabilities
- Additional platforms
- Analytics dashboard
- Template library

### Migration Guide

N/A - First release

### Breaking Changes

N/A - First release
