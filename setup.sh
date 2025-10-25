#!/bin/bash
# CarbonTrack Promoter AI Agent - Setup Script
# This script helps you get started quickly

set -e

echo "🌱 CarbonTrack Promoter AI Agent - Setup"
echo "========================================"
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found Python $python_version"

if ! python3 -c 'import sys; exit(0 if sys.version_info >= (3, 9) else 1)'; then
    echo "❌ Python 3.9 or higher is required"
    exit 1
fi

echo "✅ Python version OK"
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate || . venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip -q
echo "✅ pip upgraded"
echo ""

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt -q
echo "✅ Dependencies installed"
echo ""

# Install Playwright browsers
echo "🎭 Installing Playwright browsers..."
playwright install chromium
echo "✅ Playwright browsers installed"
echo ""

# Create .env file
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "📝 Please edit .env file with your credentials:"
    echo "   - For Ollama: Make sure Ollama is running"
    echo "   - For Grok: Add your API key"
    echo "   - For LinkedIn: Add your access token and user ID"
else
    echo "ℹ️  .env file already exists"
fi
echo ""

# Check Ollama
echo "🤖 Checking Ollama..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed"
    if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo "✅ Ollama is running"
    else
        echo "⚠️  Ollama is not running. Start it with: ollama serve"
    fi
else
    echo "⚠️  Ollama not found. Install from: https://ollama.ai"
    echo "   Or use Grok by setting LLM_PROVIDER=grok in .env"
fi
echo ""

# Create output directory
echo "📁 Creating output directory..."
mkdir -p output
echo "✅ Output directory ready"
echo ""

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. (Optional) Configure your .env file"
echo ""
echo "3. Run the agent:"
echo "   python src/main.py                    # Use example data"
echo "   python src/main.py --interactive      # Interactive mode"
echo "   python src/main.py --input examples/sample_input.json"
echo ""
echo "For more information, see:"
echo "   - README.md"
echo "   - QUICKSTART.md"
echo ""
echo "Happy promoting! 🚀"
