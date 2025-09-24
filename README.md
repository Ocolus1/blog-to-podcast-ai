# Blog-to-Podcast AI Converter

🎙️ **Transform your written content into engaging audio experiences with the power of AI!**

This project leverAGES the power of CrewAI to orchestrate multiple AI agents that work together to convert blog posts into engaging podcast content. The system scrapes blog content, processes it into a conversational script, and generates high-quality audio using advanced text-to-speech technology.

## 🚀 Features

- **🕷️ Smart Web Scraping**: Uses Firecrawl API to extract clean, structured content from any blog URL
- **✍️ Content Processor**: Creates engaging scripts with GPT-4o
- **🎤 Professional Audio Generation**: OpenAI's TTS creates natural-sounding podcast episodes
- **🎭 Multiple Voice Options**: Choose from 6 different AI voices (alloy, echo, fable, onyx, nova, shimmer)
- **💰 Cost-Effective**: Typical conversion costs under $0.20 per blog post
- **📱 Multiple Interfaces**: Interactive CLI, command-line arguments, or programmatic usage
- **⚡ Fast Processing**: Complete blog-to-podcast conversion in minutes

## 🛠️ Installation

### Prerequisites
- Python 3.10-3.13
- OpenAI API Key (set as `OPENAI_API_KEY` in .env)

### Setup

1. **Clone and navigate to the project:**
```bash
git clone https://github.com/awole/blog_to_podcast.git
cd blog_to_podcast
```
2. **Install dependencies:**
```bash
pip install uv
uv pip install -e .
```
*or*
```bash
pip install -e .
```
3. **Set up environment variables:**
Create or update your `.env` file with:
```env
OPENAI_API_KEY=your_openai_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
MODEL=gpt-4o
```

## 📖 Usage

### Method 1: 🌐 Web Interface (Recommended)
**Easiest way to use the converter with a beautiful UI!**

**Quick Launch:**
```bash
python run_app.py
```
*or on Windows, double-click:*
```bash
launch_app.bat
```

**Manual Launch:**
```bash
streamlit run app.py
```

**Features:**
- 🎨 Beautiful, modern web interface
- 🎛️ Interactive voice selection with previews  
- 📊 Real-time progress tracking
- 🎵 Built-in audio player and downloads
- 📱 Mobile-friendly responsive design
- ⚙️ Settings and API key status dashboard

### Method 2: Interactive CLI
```bash
blog_to_podcast
```
The system will prompt you for:
- Blog URL to convert
- Voice preference (optional)

### Method 3: Command Line Arguments
```bash
blog2podcast --url https://example.com/blog-post --voice nova
```

### Method 4: Direct Python Usage
```python
from blog_to_podcast.main import run_cli
result = run_cli("https://example.com/blog-post", voice="alloy")
```

### Method 5: CrewAI Integration
```bash
crewai run
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
├── podcast_script.txt
└── podcast_audio_info.txt
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

### Add Custom Tools
Create new tools in `src/blog_to_podcast/tools/` following the existing patterns.

## 📊 Performance

- **Speed**: 2-5 minutes per blog post
- **Quality**: Professional podcast-ready audio
- **Accuracy**: High-fidelity content preservation
- **Scalability**: Supports batch processing

## 🐛 Troubleshooting

### Common Issues

**1. API Key Errors**
```
Error: OPENAI_API_KEY not found in environment variables
```
→ Check your `.env` file has the correct API keys

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

- [CrewAI Documentation](https://docs.crewai.com)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Firecrawl API Docs](https://docs.firecrawl.dev)
