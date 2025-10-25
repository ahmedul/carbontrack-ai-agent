# 🌱 CarbonTrack Promoter AI Agent

An open-source AI agent that autonomously promotes your projects on LinkedIn. Built with LangChain, it generates engaging posts, creates demo videos, and publishes them to LinkedIn automatically.

## ✨ Features

- 🤖 **AI-Powered Post Generation**: Uses open-source LLMs (Ollama/Grok) to create compelling LinkedIn posts
- 🎥 **Automated Demo Videos**: Captures website demos using Playwright
- 📱 **LinkedIn Publishing**: Automatically posts content to LinkedIn with text and video
- 🔧 **Fully Customizable**: Configure tone, style, and posting schedule
- 🌍 **100% Open Source**: Built with open-source tools and MIT licensed

## 🏗️ Architecture

CarbonTrack Promoter uses a **LangChain agent** to orchestrate three main tools:

1. **Post Generator** - Creates LinkedIn post text using LLM
2. **Video Creator** - Records website demos with Playwright
3. **LinkedIn Poster** - Publishes content via LinkedIn API

```
User Input (Website URL, Description)
         ↓
   LangChain Agent
         ↓
   ┌─────┴─────┬─────────────┐
   ↓           ↓             ↓
Generate    Create       Post to
  Post      Video       LinkedIn
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Ollama installed (for local LLM) or Grok API key
- LinkedIn Developer Account (for API access)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ahmedul/carbontrack-ai-agent.git
   cd carbontrack-ai-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

4. **Configure your settings**
   Edit `src/config.py` or use environment variables for:
   - LLM provider (Ollama/Grok)
   - LinkedIn API credentials
   - Target website URL

### Usage

**Basic usage:**
```bash
python src/main.py
```

**With custom input:**
```bash
python src/main.py --input examples/sample_input.json
```

**Example input JSON:**
```json
{
  "website_url": "https://yourproject.com",
  "project_name": "CarbonTrack",
  "description": "A sustainability tracking app",
  "key_features": ["Carbon footprint tracking", "AI recommendations"],
  "tone": "professional"
}
```

## 📦 Project Structure

```
carbontrack-ai-agent/
├── README.md              # This file
├── LICENSE                # MIT license
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── src/
│   ├── main.py            # Entry point
│   ├── agent.py           # LangChain agent orchestration
│   ├── config.py          # Configuration management
│   └── tools/             # Agent tools
│       ├── __init__.py
│       ├── generate_post.py    # Post generation tool
│       ├── create_video.py     # Video recording tool
│       └── post_to_linkedin.py # LinkedIn publishing tool
├── examples/
│   └── sample_input.json  # Example input
└── .gitignore
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```env
# LLM Configuration
LLM_PROVIDER=ollama  # or 'grok'
OLLAMA_MODEL=llama2
GROK_API_KEY=your_grok_api_key

# LinkedIn API
LINKEDIN_ACCESS_TOKEN=your_access_token
LINKEDIN_USER_ID=your_user_id

# Video Settings
VIDEO_DURATION=30
VIDEO_RESOLUTION=1920x1080
```

### Customization

Modify `src/config.py` to customize:
- Post templates and styles
- Video recording settings
- Posting schedule
- Content filters

## 🛠️ Development

### Running Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black src/
flake8 src/
```

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with these amazing open-source projects:

- [LangChain](https://github.com/langchain-ai/langchain) - Agent orchestration
- [Ollama](https://ollama.ai/) - Local LLM runtime
- [Playwright](https://playwright.dev/) - Browser automation
- [python-linkedin-v2](https://github.com/linkedin-developers/linkedin-api-python-client) - LinkedIn API client

## 🤝 Support

- 📫 Issues: [GitHub Issues](https://github.com/ahmedul/carbontrack-ai-agent/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/ahmedul/carbontrack-ai-agent/discussions)
- ⭐ Star this repo if you find it helpful!

## 🗺️ Roadmap

- [ ] Multi-platform support (Twitter, Facebook)
- [ ] Scheduling system for posts
- [ ] Analytics dashboard
- [ ] Template library for different industries
- [ ] A/B testing for post variations
- [ ] Integration with more LLM providers

---

**Made with ❤️ for the open-source community**