# CarbonTrack Promoter AI Agent - Project Summary

## 🎯 Project Overview

**CarbonTrack Promoter** is a fully open-source AI agent that automates LinkedIn promotion for your projects. Built with modern AI technologies, it generates compelling posts, creates demo videos, and publishes them to LinkedIn—all automatically.

## 📁 Project Structure

```
carbontrack-ai-agent/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── src/
│   ├── __init__.py             # Package initialization
│   ├── main.py                 # CLI entry point
│   ├── agent.py                # LangChain agent orchestration
│   ├── config.py               # Configuration management
│   └── tools/
│       ├── __init__.py
│       ├── generate_post.py    # LLM-powered post generation
│       ├── create_video.py     # Playwright video recording
│       └── post_to_linkedin.py # LinkedIn API integration
├── examples/
│   ├── sample_input.json       # Professional tone example
│   ├── sample_technical.json   # Technical tone example
│   └── sample_enthusiastic.json # Enthusiastic tone example
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
├── QUICKSTART.md               # Quick start guide
├── README.md                   # Main documentation
├── requirements.txt            # Python dependencies
└── setup.py                    # Package setup
```

## 🔧 Key Technologies

### AI & Orchestration
- **LangChain**: Agent framework for orchestrating AI tools
- **Ollama**: Local open-source LLM runtime (default)
- **Grok/xAI**: Cloud-based LLM alternative
- **Pydantic**: Configuration and data validation

### Automation
- **Playwright**: Headless browser for video recording
- **OpenCV**: Video format conversion
- **LinkedIn API**: Content publishing

### Development
- **Rich**: Beautiful CLI output
- **Typer**: Modern CLI framework
- **pytest**: Testing framework
- **Black**: Code formatting

## 🚀 Features

### 1. AI-Powered Post Generation
- Multiple tone options (professional, casual, enthusiastic, technical)
- Customizable templates
- LLM-powered content creation
- Character limit enforcement

### 2. Automated Demo Videos
- Records website interactions
- Smooth scrolling animations
- Configurable duration and resolution
- Multiple video format support

### 3. LinkedIn Publishing
- Text posts with rich formatting
- Image attachment support
- Video upload capability
- Draft mode for review before posting

### 4. Flexible Configuration
- Environment variable support
- Multiple LLM provider options
- Customizable post styles
- Safe defaults for testing

## 📊 Architecture

```
User Input (JSON/CLI)
        ↓
   Main CLI (main.py)
        ↓
   CarbonTrack Agent (agent.py)
        ↓
   ┌────┴────┬──────────────┐
   ↓         ↓              ↓
Generate   Create        Post to
Post       Video        LinkedIn
(LLM)      (Playwright)  (API)
```

## 🔐 Security & Privacy

- **Environment variables** for all credentials
- **No hardcoded secrets**
- **Auto-post disabled by default**
- **Preview mode** for content review
- **.gitignore** configured for sensitive files

## 📈 Getting Started

### Minimal Setup
```bash
git clone https://github.com/ahmedul/carbontrack-ai-agent.git
cd carbontrack-ai-agent
pip install -r requirements.txt
playwright install chromium
python src/main.py  # Uses example data
```

### Production Setup
1. Install Ollama or get Grok API key
2. Configure LinkedIn credentials
3. Customize `.env` file
4. Run with `--input` for custom projects

## 🎨 Customization Points

### Post Templates
Edit `src/config.py` → `POST_TEMPLATES` dictionary

### Video Settings
Modify `.env`:
- `VIDEO_DURATION`
- `VIDEO_RESOLUTION`
- `VIDEO_FPS`

### Agent Behavior
Adjust in `src/agent.py`:
- System prompt
- Tool selection logic
- Error handling

## 🧪 Testing

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Check coverage
pytest --cov=src tests/

# Format code
black src/

# Lint
flake8 src/
```

## 🌟 Use Cases

1. **Product Launches**: Automate promotional posts for new releases
2. **Content Marketing**: Schedule regular project updates
3. **Developer Portfolio**: Showcase your projects professionally
4. **Open Source Projects**: Promote community contributions
5. **Startups**: Cost-effective social media automation

## 🛣️ Roadmap

- [ ] Multi-platform support (Twitter/X, Facebook, Instagram)
- [ ] Scheduling system for automated posts
- [ ] Analytics and engagement tracking
- [ ] A/B testing for post variations
- [ ] Template marketplace
- [ ] Web dashboard
- [ ] Docker deployment
- [ ] API mode for integrations

## 📝 License

MIT License - completely open source and free to use, modify, and distribute.

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/ahmedul/carbontrack-ai-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ahmedul/carbontrack-ai-agent/discussions)
- **Documentation**: [README.md](README.md) & [QUICKSTART.md](QUICKSTART.md)

---

**Built with ❤️ by the open-source community**

**Version**: 0.1.0  
**Status**: Alpha  
**Last Updated**: October 25, 2025
