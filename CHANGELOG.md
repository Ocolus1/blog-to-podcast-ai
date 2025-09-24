# CHANGELOG

All notable changes to this project will be documented in this file.

## [1.1.1] - 2025-01-25 - UI Download Fix

### Bug Fixes
- **CRITICAL FIX**: Resolved UI reset issue when downloading audio files or podcast scripts
- **Root Cause**: Streamlit was rerunning the entire app on download button clicks, losing conversion results
- **Solution**: Implemented `st.session_state` to persist conversion results across app reruns
- **Enhancement**: Added "Clear Results" button to allow users to start fresh conversions
- **UX Improvement**: Added helpful tip indicating downloads won't reset the page

### Technical Changes
- Added session state management for `last_conversion_files` and `last_conversion_successful`
- Improved conversion result persistence using Streamlit session state
- Enhanced user experience with download persistence and clear results functionality

## [1.1.0] - 2025-01-25 - Production Ready Release

### Code Cleanup & Production Preparation
- **Environment Variables**: Standardized to use `OPENAI_API_KEY` instead of `OPEN_API_KEY` for consistency with OpenAI library standards
- **Debug Cleanup**: Removed debug print statements from `main.py` CLI module
- **Git Ignore**: Enhanced `.gitignore` with comprehensive production-ready exclusions:
  - Python cache files, distribution packages, virtual environments
  - IDE files, OS-specific files, logs, temporary files
  - Output files (keeps directory structure but ignores generated content)
  - Coverage reports and testing artifacts
- **Cache Cleanup**: Removed all `__pycache__` directories and `.pyc` files from repository
- **Error Handling**: Improved error handling in CLI with proper exception propagation
- **Code Organization**: Removed unnecessary comments and optimized spacing in codebase

### Documentation Updates
- **README.md**: Updated API key references to use standard `OPENAI_API_KEY` format
- **.env.example**: Cleaned up and standardized environment variable naming
- **Error Messages**: Updated all error messages to reference correct environment variable names

### Files Modified
- `src/blog_to_podcast/main.py` - Removed debug prints, improved error handling
- `src/blog_to_podcast/tools/content_processor.py` - Updated API key references
- `src/blog_to_podcast/tools/audio_generator.py` - Updated API key references  
- `run_app.py` - Updated environment variable validation
- `app.py` - Updated API key configuration display
- `.gitignore` - Comprehensive production-ready exclusions
- `.env.example` - Standardized variable naming
- `README.md` - Updated documentation for consistency

### Production Readiness
This release makes the codebase ready for:
- GitHub repository publication
- Production deployment
- Clean development environment setup
- Standardized API key management

## [0.1.0] - 2024-09-24

### Added
- Initial implementation of blog-to-podcast conversion system
- **Custom Tools Created:**
  - `Firecrawl Scraper`: Web scraping tool using Firecrawl API for clean blog content extraction
  - `FirecrawlScraper`: Web scraping tool using Firecrawl API for clean blog content extraction
  - `ContentProcessor`: OpenAI GPT-4 powered script generator for podcast content
  - `AudioGenerator`: OpenAI TTS integration for high-quality audio generation
- **Specialized AI Agents:**
  - `blog_scraper`: Expert web content scraper for blog post extraction
  - `content_processor`: Podcast script writer and content strategist
  - `audio_producer`: Professional audio producer and voice synthesis specialist
- **Sequential Workflow Tasks:**
  - `blog_scraping_task`: Clean blog content extraction with metadata
  - `script_generation_task`: Conversational podcast script generation (3-7 minutes)
  - `audio_generation_task`: Professional MP3 audio file generation
- **Multiple Usage Options:**
  - Interactive CLI with voice selection
  - Command-line interface with argparse support
  - Direct function calls for integration
- **Voice Options:** Support for 6 OpenAI TTS voices (alloy, echo, fable, onyx, nova, shimmer)
- **Cost Optimization:** Using OpenAI TTS-1 model for cost-effective audio generation (~$0.015 per 1K characters)
- **Output Management:** Organized file structure with audio files saved to `output/audio/` directory
- **Error Handling:** Comprehensive error handling with user-friendly messages
- **Dependencies:** Added OpenAI, Requests, and Pydantic to project requirements

### Technical Details
- **Framework:** Built on CrewAI for multi-agent orchestration
- **APIs Used:** 
  - Firecrawl API for web scraping
  - OpenAI GPT-4o for content processing
  - OpenAI TTS-1 for audio generation
- **File Structure:** Modular design with separate tools, agents, and tasks
- **Configuration:** YAML-based agent and task configuration
- **Entry Points:** Multiple CLI commands via pyproject.toml scripts

### Files Modified/Created
- `src/blog_to_podcast/tools/firecrawl_scraper.py` (new)
- `src/blog_to_podcast/tools/content_processor.py` (new)
- `src/blog_to_podcast/tools/audio_generator.py` (new)
- `src/blog_to_podcast/tools/__init__.py` (updated)
- `src/blog_to_podcast/config/agents.yaml` (completely rewritten)
- `src/blog_to_podcast/config/tasks.yaml` (completely rewritten)
- `src/blog_to_podcast/crew.py` (updated with new agents and tasks)
- `src/blog_to_podcast/main.py` (updated with CLI and interactive features)
- `pyproject.toml` (updated dependencies and scripts)
- `CHANGELOG.md` (new)
- `README.md` (updated with usage instructions)

## [0.2.0] - 2024-09-24

### Added - Streamlit Web Interface
- **🌐 Amazing Web UI**: Beautiful Streamlit web application with modern design
- **🎨 Custom Styling**: Gradient backgrounds, hover effects, and professional visual design
- **🎛️ Interactive Controls**: 
  - Voice selection with visual cards and descriptions
  - Real-time progress tracking with animated progress bars
  - Auto-play and detailed progress toggle options
- **📊 Dashboard Features**:
  - Session statistics tracking
  - Conversion counter
  - API key status indicators
  - File management dashboard
- **🎵 Audio Experience**:
  - Built-in audio player for immediate playback
  - One-click MP3 downloads
  - File size and quality information
  - Auto-play functionality
- **📚 User Experience**:
  - Tabbed interface (Convert, Examples, Settings)
  - Quick example URL buttons
  - Comprehensive help and troubleshooting
  - Success celebrations with balloons animation
- **🚀 Easy Launch Options**:
  - `run_app.py`: Python launcher with dependency checking
  - `launch_app.bat`: Windows batch file for one-click launch
  - Streamlit configuration with custom theming

### Technical Enhancements
- **Dependencies**: Added Streamlit and pathlib2 to requirements
- **Configuration**: Custom Streamlit theme with brand colors (#667eea primary)
- **Error Handling**: User-friendly error messages with troubleshooting tips
- **File Management**: Automatic detection of generated audio and script files
- **Cross-Platform**: Works on Windows, macOS, and Linux

### Usage Methods (Updated)
1. **Web Interface**: `python run_app.py` or `streamlit run app.py`
2. **Windows Launcher**: Double-click `launch_app.bat`
3. **Interactive CLI**: `blog_to_podcast`
4. **Command Line**: `blog2podcast --url https://example.com --voice nova`
5. **Direct Python**: Import and use functions programmatically

### Files Added
- `app.py` (new) - Main Streamlit web application
- `run_app.py` (new) - Smart launcher with dependency checking
- `launch_app.bat` (new) - Windows batch launcher
- `.streamlit/config.toml` (new) - Streamlit configuration and theming
- `requirements.txt` (new) - Standalone requirements file

## [2025-01-24] - Bug Fix: Module Import and Tool Errors

### Fixed
- **CRITICAL BUG FIX**: Resolved "Error during conversion: 'FirecrawlScraper'" issue
- **CRITICAL BUG FIX**: Resolved "Cannot import blog_to_podcast module: No module named 'blog_to_podcast'" issue
- **CRITICAL BUG FIX**: Resolved "AuthenticationError: OpenAIException - The api_key client option must be set" issue
- **CRITICAL BUG FIX**: Resolved "'Firecrawl' object has no attribute 'scrape_url'" web scraping error
- Root cause 1: Tool naming conflict between custom FirecrawlScraper and CrewAI's built-in tool registry
- Root cause 2: Package not installed in development mode, causing import failures
- Root cause 3: OpenAI library expects `OPENAI_API_KEY` environment variable, but application used `OPEN_API_KEY`
- Root cause 4: Built-in FirecrawlScrapeWebsiteTool uses outdated method `scrape_url` instead of correct `scrape` method
- Solution 1: Initially replaced with CrewAI's built-in FirecrawlScrapeWebsiteTool, then reverted to fixed custom FirecrawlScraper
- Solution 2: Installed package in development mode using `pip install -e .`
- Solution 3: Added both `OPEN_API_KEY` and `OPENAI_API_KEY` to .env for full compatibility
- Solution 4: Updated custom FirecrawlScraper to use correct `scrape` method and proper response handling
- Added missing `firecrawl-py>=4.3.6` dependency to both requirements.txt and pyproject.toml

### Technical Changes
- **crew.py**: Reverted back to custom `FirecrawlScraper` after fixing the method calls
- **firecrawl_scraper.py**: Updated to use `FirecrawlApp.scrape()` instead of REST API calls and fixed response handling
- **agents.yaml**: Removed tool specifications from YAML (tools now instantiated directly in code)
- **requirements.txt**: Added firecrawl-py dependency
- **pyproject.toml**: Updated dependencies, removed pathlib2 (not needed for Python 3.10+), added python-dotenv
- **.env**: Added both `OPEN_API_KEY` and `OPENAI_API_KEY` environment variables for compatibility
- **.env.example**: Updated to include both API key variants with explanation
- **Package Installation**: Installed in development mode using `pip install -e .`

### Files Modified
- `src/blog_to_podcast/crew.py`
- `src/blog_to_podcast/tools/firecrawl_scraper.py`
- `src/blog_to_podcast/config/agents.yaml`
- `requirements.txt`
- `pyproject.toml`
- `.env`
- `.env.example`

### What Caused the Errors
1. **FirecrawlScraper Error**: The custom FirecrawlScraper tool was being referenced in agents.yaml, but CrewAI's tool registry couldn't find it because the tool name didn't match the registry's expectations. The built-in FirecrawlScrapeWebsiteTool is more robust and actively maintained.

2. **Module Import Error**: The `blog_to_podcast` package wasn't installed in development mode, so Python couldn't find the module when importing. The package structure was correct, but it needed to be installed using `pip install -e .` to make it importable.

3. **OpenAI API Key Error**: The OpenAI library automatically looks for the `OPENAI_API_KEY` environment variable when no API key is explicitly provided to the client. The application was using `OPEN_API_KEY` but some parts of the codebase were using the default OpenAI client initialization, causing authentication failures.

4. **Firecrawl Scraping Error**: The built-in `FirecrawlScrapeWebsiteTool` uses the outdated method name `scrape_url`, but the current firecrawl-py library uses `scrape`. This caused the scraping to fail completely, resulting in generic podcast content instead of actual blog content.

## [2025-01-24] - File Organization Improvement

### Added
- **Organized Output Directory Structure**: Created clean, organized folder structure for all generated files
- **Automatic Directory Creation**: All necessary directories are created automatically on first use
- **Enhanced File Management**: Better tracking and display of generated files by type

### New Directory Structure
```
output/
├── scripts/     # Podcast scripts (.txt files)
├── audio/       # Audio files (.mp3 files)
└── metadata/    # Info files and metadata
```

### Technical Changes
- **crew.py**: Added automatic directory creation in `__init__()` and updated script output path
- **tasks.yaml**: Updated `podcast_audio_info.txt` to save in `output/metadata/` 
- **audio_generator.py**: Enhanced to create all necessary directories
- **app.py**: Updated file finding logic to work with organized structure and improved directory display

### Files Modified
- `src/blog_to_podcast/crew.py`
- `src/blog_to_podcast/config/tasks.yaml`
- `src/blog_to_podcast/tools/audio_generator.py`
- `app.py`

## [2025-01-24] - Multi-Part Audio Display Fix

### Fixed
- **CRITICAL BUG FIX**: Resolved issue where only the last audio part was shown when multi-part podcasts were generated
- **Enhanced User Experience**: Users can now access all parts of their podcast content instead of missing 75% of it
- **Improved Multi-Part Detection**: Smart detection and grouping of related audio files from the same generation session

### Root Cause
The `find_generated_files()` function was using `max(audio_files, key=os.path.getctime)` which only returned the most recent file (e.g., "part4") instead of finding all related parts of the same podcast episode.

### Solution
1. **Enhanced File Detection**: Updated logic to detect and group all related audio files by base name pattern
2. **Multi-Part Display**: Added proper UI to display all audio parts with individual players and download buttons  
3. **Smart Sorting**: Audio parts are automatically sorted in correct order (Part 1, Part 2, Part 3, Part 4)
4. **User-Friendly Interface**: Added expandable sections for each part with clear labeling

### New Features
- **Multi-Part Audio Support**: Displays all audio files when content is split into multiple parts
- **Individual Part Players**: Each part has its own audio player and download button
- **Total Statistics**: Shows total file count and combined size for multi-part podcasts
- **Sequential Organization**: Parts are displayed in correct listening order
- **Backward Compatibility**: Single-file podcasts continue to work as before

### Technical Changes
- **`find_generated_files()`**: Updated to return list of related audio files instead of single file
- **`display_results()`**: Enhanced to handle both single and multi-part audio display
- **Multi-Part Detection**: Added logic to detect "_part" pattern and group related files
- **UI Enhancement**: Added expandable sections and improved file information display

### Files Modified
- `app.py`

### Requirements
- Python 3.10-3.13
- OpenAI API Key (set as `OPEN_API_KEY` in .env)
- Firecrawl API Key (set as `FIRECRAWL_API_KEY` in .env)
