# Contributing to YouTube Video Summarizer

Thank you for your interest in contributing! This document provides guidelines and setup instructions.

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Docker (optional, for containerized development)
- FFmpeg
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Youtube-Video-Summarizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Production dependencies
   pip install -r requirements.txt

   # Development dependencies (includes testing, linting, etc.)
   pip install -r requirements-dev.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   # Development mode
   export FLASK_DEBUG=True
   python app.py

   # Or with Gunicorn (production-like)
   gunicorn --bind 0.0.0.0:5000 --workers 2 app:app
   ```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=videosum --cov-report=html

# View coverage report
open htmlcov/index.html
```

## 🎨 Code Quality

### Formatting
```bash
# Format code with Black
black .

# Check formatting without changes
black --check .
```

### Linting
```bash
# Run Flake8
flake8 .

# Run Pylint
pylint videosum/ app.py
```

### Type Checking
```bash
# Run MyPy
mypy videosum/ app.py
```

### Security Scanning
```bash
# Run Bandit
bandit -r videosum/ app.py

# Check dependencies for vulnerabilities
safety check
```

## 🐳 Docker Development

```bash
# Build the image
docker build -t youtube-video-summarizer:dev .

# Run the container
docker run -d -p 5000:5000 youtube-video-summarizer:dev

# Check health
curl http://localhost:5000/health
```

## 📝 Commit Guidelines

We follow conventional commits:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

Example:
```
feat: add support for multiple video formats
fix: resolve yt-dlp download timeout issue
docs: update installation instructions
```

## 🔀 Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters
5. Commit your changes
6. Push to your fork
7. Open a Pull Request

### PR Checklist
- [ ] Code follows project style (Black formatting)
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] No security vulnerabilities introduced
- [ ] CHANGELOG updated (if applicable)

## 🐛 Reporting Bugs

Please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

## 💡 Suggesting Features

Open an issue with:
- Clear description of the feature
- Use cases
- Potential implementation approach
- Any relevant examples

## 📚 Development Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [Transformers (HuggingFace)](https://huggingface.co/docs/transformers)

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## ❓ Questions?

Feel free to open an issue for any questions or clarifications!
