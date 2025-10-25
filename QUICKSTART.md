# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Install Ollama (for local LLM)

**macOS/Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama2
```

**Windows:**
Download from [ollama.ai](https://ollama.ai/download)

### 2. Clone and Setup

```bash
git clone https://github.com/ahmedul/carbontrack-ai-agent.git
cd carbontrack-ai-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
playwright install chromium
```

### 3. Configure

```bash
cp .env.example .env
# Edit .env with your settings (optional for basic testing)
```

**Minimum configuration for testing:**
```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama2
AUTO_POST=false  # Keep false for testing
```

### 4. Run!

**Basic run with example data:**
```bash
python src/main.py
```

**With custom input:**
```bash
python src/main.py --input examples/sample_input.json
```

**Interactive mode:**
```bash
python src/main.py --interactive
```

## 🔧 Next Steps

### Enable LinkedIn Posting

1. Create a LinkedIn App at [LinkedIn Developers](https://www.linkedin.com/developers/apps)
2. Get your access token and user ID
3. Update `.env`:
   ```env
   LINKEDIN_ACCESS_TOKEN=your_token
   LINKEDIN_USER_ID=your_user_id
   AUTO_POST=true  # Enable auto-posting
   ```

### Use Grok Instead of Ollama

1. Get API key from [x.ai](https://x.ai/)
2. Update `.env`:
   ```env
   LLM_PROVIDER=grok
   GROK_API_KEY=your_api_key
   ```

### Customize Post Style

Edit `src/config.py` to customize post templates or add your own tone styles.

## 📝 Example Workflow

```bash
# 1. Generate a post (without posting)
python src/main.py --input examples/sample_input.json

# 2. Review the generated content in output/

# 3. When ready, enable auto-posting in .env
AUTO_POST=true

# 4. Run again to post to LinkedIn
python src/main.py --input examples/sample_input.json
```

## 🆘 Troubleshooting

**Ollama connection error:**
```bash
# Make sure Ollama is running
ollama serve

# Test it
ollama run llama2 "Hello"
```

**Playwright issues:**
```bash
# Reinstall browsers
playwright install chromium --force
```

**Import errors:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📚 More Information

- Full documentation: See [README.md](README.md)
- Examples: See [examples/](examples/)
- Contributing: See [CONTRIBUTING.md](CONTRIBUTING.md)
