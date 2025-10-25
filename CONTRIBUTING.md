# Contributing to CarbonTrack Promoter

Thank you for your interest in contributing to CarbonTrack Promoter! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)

### Suggesting Features

We welcome feature suggestions! Please open an issue with:
- A clear description of the feature
- Why it would be useful
- Possible implementation approach

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting:
   ```bash
   pytest tests/
   black src/
   flake8 src/
   ```
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/carbontrack-ai-agent.git
   cd carbontrack-ai-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   playwright install chromium
   ```

4. Set up your `.env` file from `.env.example`

## Code Style

- Follow PEP 8
- Use type hints
- Write docstrings for functions and classes
- Keep functions focused and small
- Add comments for complex logic

## Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
