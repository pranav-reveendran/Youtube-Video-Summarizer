# YouTube Video Summarizer - Changelog

## [2.0.0] - 2024-12-31

### Major Updates
- Upgraded to Python 3.12 with Debian Bookworm
- Replaced deprecated PyTube with yt-dlp
- Added Gunicorn production WSGI server
- Pinned all dependencies for stability

### Added
- Health check endpoint at `/health`
- Docker HEALTHCHECK instruction
- Comprehensive CI/CD with GitHub Actions
- Development tooling (pytest, black, flake8, bandit)
- Environment configuration template
- Contributing guidelines
- Security scanning workflows

### Changed
- Flask debug mode now environment-controlled
- Enhanced Dependabot configuration
- Improved .dockerignore and .gitignore
- Updated README with modern tech stack

### Security
- Fixed debug mode security issue
- Added automated dependency scanning
- Enhanced Docker security practices
- Regular security audits via GitHub Actions
