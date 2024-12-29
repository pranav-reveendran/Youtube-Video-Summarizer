# **Speech-To-Text Transcription and Summarization Web Application**

This project develops a web application that enables users to upload videos or provide video links to automatically transcribe audio into text. The application also offers translation options and generates a concise summary of the video's content. Built using modern Python frameworks with production-ready configurations.

## 🎯 **Tech Stack (2025-Ready)**

### **Core Framework**
- **Python 3.12** - Latest stable Python with performance improvements
- **Flask 3.0** - Modern web framework
- **Gunicorn** - Production-grade WSGI server

### **AI/ML Models**
- **OpenAI Whisper** - State-of-the-art speech recognition (pinned version)
- **BART-Large-CNN** - Advanced text summarization via HuggingFace Transformers
- **PyTorch 2.1** - Latest ML framework backend

### **Video Processing**
- **yt-dlp** - Robust, actively maintained YouTube downloader (replaces deprecated PyTube)
- **FFmpeg** - Industry-standard media processing

### **Infrastructure**
- **Docker** - Containerization with optimized multi-layer caching
- **Python 3.12-slim-bookworm** - Modern, secure Debian base
- **CircleCI** - Automated CI/CD pipeline
- **AWS ECR/EC2** - Cloud deployment with container registry

### **Security & Maintenance**
- **Dependabot** - Automated dependency updates for pip, Docker, and devcontainers
- **Pinned versions** - All dependencies locked to specific versions
- **Enhanced .dockerignore** - Optimized build context and security

### 🚀 **Key Components**
- **🎥 Video Downloader**: Downloads videos from YouTube or accepts video files uploaded by the user using the robust `yt-dlp` library.
- **💬 Subtitle Generator**: Transcribes video audio using `OpenAI's Whisper model` with translation capabilities.
- **📝 Summarizer**: Summarizes the transcribed text using the `BART-Large model`.

### 🌐 **Deployment**
- **Containerization**: The application is packaged with `Docker` using Python 3.12 and optimized build layers.
- **CI/CD**: `CircleCI` automates building, testing, and deploying the application to `AWS EC2`, ensuring continuous integration and deployment.
- **Production Server**: Runs with `Gunicorn` WSGI server for production workloads (configurable workers and timeouts).

### 🛠️ **How to Run?**
1. **Clone the Repository**:
   ```bash
   git clone <repository-link>

