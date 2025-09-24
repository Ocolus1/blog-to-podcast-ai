# Blog-to-Podcast AI Converter

🎙️ **Transform your written content into engaging audio experiences with the power of AI!**

This project leverages the power of CrewAI to orchestrate multiple AI agents that work together to convert blog posts into engaging podcast content. The system scrapes blog content, processes it into a conversational script, and generates high-quality audio using advanced text-to-speech technology.

## 🚀 Features

- **🕷️ Smart Web Scraping**: Uses Firecrawl API to extract clean, structured content from any blog URL
- **✍️ Content Processor**: Creates engaging scripts with GPT-4o
- **🎤 Professional Audio Generation**: OpenAI's TTS creates natural-sounding podcast episodes
- **🎭 Multiple Voice Options**: Choose from 6 different AI voices (alloy, echo, fable, onyx, nova, shimmer)
- **💰 Cost-Effective**: Typical conversion costs under $0.20 per blog post
- **📱 Multiple Interfaces**: Interactive CLI, command-line arguments, or programmatic usage
- **⚡ Fast Processing**: Complete blog-to-podcast conversion in minutes
- **🎨 Modern Web UI**: Beautiful Streamlit interface with real-time progress tracking
- **💾 Persistent Downloads**: Download all generated files without losing UI state

## 🛠️ Installation

### Prerequisites
- Python 3.10-3.13 (3.14 not supported)
- OpenAI API Key (set as `OPENAI_API_KEY` in .env)
- Firecrawl API Key (set as `FIRECRAWL_API_KEY` in .env)

### Setup

1. **Clone and navigate to the project:**
```bash
git clone https://github.com/Ocolus1/blog-to-podcast-ai.git
cd blog-to-podcast-ai
```
2. **Install dependencies:**

**Method 1 - Using UV (Recommended):**
```bash
# Install UV package manager
pip install uv

# Install project dependencies
uv pip install -e .
```

**Method 2 - Using pip:**
```bash
pip install -e .
```

**Method 3 - Direct from pyproject.toml:**
```bash
pip install .
```
3. **Set up environment variables:**
Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

Then edit your `.env` file:
```env
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here

# Model Configuration
MODEL=gpt-4o

# Optional Audio Settings
AUDIO_SPEED=1.0
AUDIO_PITCH=0.0
```

## 📖 Usage

### Method 1: 🌐 Web Interface (Recommended)
**Easiest way to use the converter with a beautiful UI!**

**Quick Launch (Recommended):**
```bash
python run_app.py
```
*or on Windows, double-click:*
```bash
launch_app.bat
```

**Direct Streamlit Launch:**
```bash
streamlit run app.py
```

**Alternative Streamlit Command:**
```bash
# If streamlit is not in PATH, use python -m
python -m streamlit run app.py

# Specify custom port (default is 8501)
streamlit run app.py --server.port 8080

# Run on specific address
streamlit run app.py --server.address 0.0.0.0
```

**🌐 Accessing the Web Interface:**
After running any of the above commands, your browser should automatically open to:
- **Local URL**: http://localhost:8501
- **Network URL**: http://your-ip-address:8501 (for external access)

If the browser doesn't open automatically, copy and paste the URL from the terminal.

**Features:**
- 🎨 Beautiful, modern web interface
- 🎛️ Interactive voice selection with previews  
- 📊 Real-time progress tracking
- 🎵 Built-in audio player and downloads
- 📱 Mobile-friendly responsive design
- ⚙️ Settings and API key status dashboard
- 💾 Persistent download state (fixed: downloads no longer reset the UI)
- 🗂️ "Clear Results" button for easy session management

### Method 2: Interactive CLI
```bash
blog_to_podcast
```
The system will prompt you for:
- Blog URL to convert
- Voice preference (optional)

### Method 3: Command Line Arguments
```bash
# Using the blog2podcast command
blog2podcast --url https://example.com/blog-post --voice nova

# Alternative using Python module
python -m blog_to_podcast.main --url https://example.com/blog-post --voice nova
```

### Method 4: Direct Python Usage
```python
from blog_to_podcast.main import run_cli
result = run_cli("https://example.com/blog-post", voice="alloy")
```

### Method 5: CrewAI Integration
```bash
# Run using CrewAI CLI
crewai run

# Or use the run_crew script command
run_crew
```

## 🎭 Voice Options

Choose from 6 high-quality AI voices:
- **alloy** (default) - Balanced, natural tone
- **echo** - Clear, professional sound
- **fable** - Warm, storytelling voice
- **onyx** - Deep, authoritative tone
- **nova** - Energetic, modern sound
- **shimmer** - Bright, engaging voice

## 🏗️ System Architecture

### AI Agents
1. **🕷️ Blog Scraper**: Extracts clean content using Firecrawl API
2. **✍️ Content Processor**: Creates engaging scripts with GPT-4o
3. **🎙️ Audio Producer**: Generates professional audio with OpenAI TTS

### Workflow
1. **Scraping** → Clean blog content extraction with metadata
2. **Processing** → Conversational script generation (3-7 minutes)
3. **Production** → High-quality MP3 audio file creation

### Output Structure
```
output/
├── audio/
│   └── podcast_20240924_143022_abc123.mp3
├── metadata/
│   ├── podcast_script.txt
│   └── podcast_audio_info.txt
└── scripts/
    └── processed_content.txt
```

## 💡 Examples

**Convert a Medium article:**
```bash
blog2podcast --url https://medium.com/@author/article --voice echo
```

**Convert a technical blog:**
```bash
blog2podcast --url https://techblog.com/deep-learning-guide --voice onyx
```

**Using Python module directly:**
```bash
python -m blog_to_podcast.main --url https://example.com/blog-post
```

## 💰 Cost Estimation

Typical costs per blog post:
- **Firecrawl scraping**: ~$0.001
- **GPT-4o processing**: ~$0.02-0.05
- **OpenAI TTS**: ~$0.015 per 1K characters
- **Total**: Usually under $0.20 per conversion

## 🔧 Customization

### Modify Agents
Edit `src/blog_to_podcast/config/agents.yaml` to customize:
- Agent roles and personalities
- Tool assignments
- Backstories and goals

### Adjust Tasks
Edit `src/blog_to_podcast/config/tasks.yaml` to modify:
- Workflow steps
- Output formats
- Task dependencies

### Current Tools Available
The project includes these specialized tools:
- **firecrawl_scraper.py**: Web content extraction
- **content_processor.py**: Script generation with GPT-4o
- **audio_generator.py**: Text-to-speech conversion
- **custom_tool.py**: Template for additional tools

### Add Custom Tools
Create new tools in `src/blog_to_podcast/tools/` following the existing patterns.

## 📊 Performance

- **Speed**: 2-5 minutes per blog post
- **Quality**: Professional podcast-ready audio
- **Accuracy**: High-fidelity content preservation
- **Scalability**: Supports batch processing

## 🆕 Recent Updates

### v0.1.0 - Latest Release
- ✅ **Modernized Dependencies**: Migrated to `pyproject.toml` with UV package manager support
- ✅ **Enhanced Audio Controls**: Added `AUDIO_SPEED` and `AUDIO_PITCH` environment variables
- ✅ **Fixed UI Download Issue**: Downloads no longer reset the Streamlit interface
- ✅ **Enhanced Session Management**: Added persistent state and "Clear Results" functionality
- ✅ **Production Ready**: Comprehensive code cleanup and optimization
- ✅ **Standardized Environment**: Updated to use `OPENAI_API_KEY` consistently
- ✅ **Improved CLI**: Better command-line interface with multiple entry points
- ✅ **Windows Compatibility**: Added troubleshooting for Visual C++ build issues

## 🐛 Troubleshooting

### Common Issues

**1. API Key Errors**
```
Error: OPENAI_API_KEY not found in environment variables
```
→ Copy `.env.example` to `.env` and add your API keys
→ Ensure both `OPENAI_API_KEY` and `FIRECRAWL_API_KEY` are set

**2. Network Timeouts**
```
Error: Request timeout while scraping
```
→ Check internet connection and try again

**3. Audio Generation Fails**
```
Error: Permission denied when writing to output directory
```
→ Ensure write permissions for the project directory

**4. Windows Build Tools Error (CrewAI Dependencies)**
```
Microsoft Visual C++ 14.0 is required. Get it with "Microsoft C++ Build Tools"
```
→ Install Microsoft C++ Build Tools from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
→ Or install Visual Studio with C++ development tools
→ Alternatively, try using conda instead of pip for installation

**5. Streamlit Issues**
```
streamlit: command not found
```
→ Try: `python -m streamlit run app.py`
→ Or ensure streamlit is installed: `pip install streamlit`

```
Port 8501 is already in use
```
→ Use a different port: `streamlit run app.py --server.port 8502`
→ Or kill the existing process and try again

**6. Dependencies Installation Issues**
```
ERROR: Could not build wheels for package
```
→ Try using UV package manager: `pip install uv && uv pip install -e .`
→ Or install build tools: `pip install build setuptools wheel`
→ For Windows: Install Microsoft C++ Build Tools

**7. Python Version Issues**
```
Requires Python >=3.10,<3.14
```
→ Use Python 3.10, 3.11, 3.12, or 3.13 (Python 3.14+ not supported)
→ Check version: `python --version`

## 📚 Advanced Usage

### Batch Processing
```python
urls = ["https://blog1.com/post", "https://blog2.com/article"]
for url in urls:
    run_cli(url, voice="alloy")
```
### Custom Voice Settings
```python
# Use different voices for variety
voices = ["alloy", "echo", "fable"]
for i, url in enumerate(urls):
    voice = voices[i % len(voices)]
    run_cli(url, voice=voice)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update CHANGELOG.md
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- **CrewAI**: Multi-agent AI framework
- **OpenAI**: GPT-4o and TTS APIs
- **Firecrawl**: Web scraping API
- **Community**: Contributors and users

## 🔗 Links

- **[🔥 GitHub Repository](https://github.com/Ocolus1/blog-to-podcast-ai.git)** - Star and fork this project!
- [CrewAI Documentation](https://docs.crewai.com)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Firecrawl API Docs](https://docs.firecrawl.dev)
