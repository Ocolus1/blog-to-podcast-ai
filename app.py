import streamlit as st
import os
import time
import asyncio
from datetime import datetime
from pathlib import Path
import base64
from typing import Optional

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    st.warning("python-dotenv not installed. Environment variables may not be loaded from .env file.")

# Set page config first
st.set_page_config(
    page_title="Blog2Podcast AI 🎙️", 
    page_icon="🎙️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import your existing functionality
try:
    from blog_to_podcast.crew import BlogToPodcast
except ImportError as e:
    st.error(f"❌ Cannot import blog_to_podcast module: {str(e)}")
    st.markdown("""
    **Possible solutions:**
    1. Run: `pip install -r requirements.txt`
    2. Make sure you're in the correct directory
    3. Check if all dependencies are installed
    4. For Windows users with build errors, run: `install_windows.bat`
    """)
    st.stop()
except Exception as e:
    st.error(f"❌ Unexpected error importing modules: {str(e)}")
    st.stop()

# Custom CSS for amazing UI
def load_css():
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .success-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stProgress .st-bo {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .audio-player {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    
    .stats-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .voice-selector {
        background: #ffffff;
        border: 2px solid #667eea;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .voice-selector:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

def create_header():
    st.markdown("""
    <div class="main-header">
        <h1>🎙️ Blog2Podcast AI Converter</h1>
        <p>Transform any blog post into a professional podcast episode using advanced AI</p>
    </div>
    """, unsafe_allow_html=True)

def create_sidebar():
    st.sidebar.markdown("## 🎛️ Control Panel")
    
    # Voice selection with visual cards
    st.sidebar.markdown("### 🎤 Select AI Voice")
    
    voices = {
        "alloy": {"desc": "Balanced, natural tone", "emoji": "🎯"},
        "echo": {"desc": "Clear, professional sound", "emoji": "🔊"},
        "fable": {"desc": "Warm, storytelling voice", "emoji": "📚"},
        "onyx": {"desc": "Deep, authoritative tone", "emoji": "🎭"},
        "nova": {"desc": "Energetic, modern sound", "emoji": "⭐"},
        "shimmer": {"desc": "Bright, engaging voice", "emoji": "✨"}
    }
    
    selected_voice = st.sidebar.selectbox(
        "Choose voice:",
        options=list(voices.keys()),
        format_func=lambda x: f"{voices[x]['emoji']} {x.title()} - {voices[x]['desc']}",
        index=0
    )
    
    # Advanced settings
    st.sidebar.markdown("### ⚙️ Advanced Settings")
    
    show_progress = st.sidebar.checkbox("Show detailed progress", value=True)
    auto_play = st.sidebar.checkbox("Auto-play generated audio", value=True)
    
    # Statistics
    st.sidebar.markdown("### 📊 Session Stats")
    if 'conversion_count' not in st.session_state:
        st.session_state.conversion_count = 0
    
    st.sidebar.metric("Conversions Today", st.session_state.conversion_count)
    
    # About section
    with st.sidebar.expander("ℹ️ About"):
        st.markdown("""
        **Blog2Podcast AI** uses:
        - 🕷️ Firecrawl for web scraping
        - 🤖 GPT-4o for script generation  
        - 🎙️ OpenAI TTS for audio synthesis
        - 🎭 CrewAI for orchestration
        
        **Typical costs**: ~$0.20 per conversion
        """)
    
    return selected_voice, show_progress, auto_play

def get_audio_download_link(file_path: str, filename: str) -> str:
    """Generate download link for audio file"""
    try:
        with open(file_path, "rb") as f:
            audio_bytes = f.read()
        b64_audio = base64.b64encode(audio_bytes).decode()
        return f'<a href="data:audio/mp3;base64,{b64_audio}" download="{filename}" class="download-btn">📥 Download MP3</a>'
    except:
        return "❌ Download not available"

def show_features():
    st.markdown("## ✨ Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🕷️ Smart Scraping</h3>
            <p>Extracts clean content from any blog URL using advanced AI-powered scraping</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI Script Writing</h3>
            <p>GPT-4o transforms blog content into engaging, conversational podcast scripts</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🎙️ Professional Audio</h3>
            <p>High-quality text-to-speech with 6 different AI voices to choose from</p>
        </div>
        """, unsafe_allow_html=True)

def run_conversion(blog_url: str, voice: str, show_progress: bool = True):
    """Run the blog-to-podcast conversion with progress tracking"""
    
    if show_progress:
        # Create progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Step 1: Initialize
        progress_bar.progress(10)
        status_text.text("🚀 Initializing conversion process...")
        time.sleep(1)
        
        # Step 2: Scraping
        progress_bar.progress(30)
        status_text.text("🕷️ Scraping blog content...")
        
    # Prepare inputs for CrewAI
    inputs = {
        'blog_url': blog_url,
        'voice': voice,
        'current_year': str(datetime.now().year)
    }
    
    try:
        if show_progress:
            progress_bar.progress(50)
            status_text.text("🤖 Generating podcast script...")
        
        # Run the CrewAI workflow
        crew = BlogToPodcast()
        result = crew.crew().kickoff(inputs=inputs)
        
        if show_progress:
            progress_bar.progress(80)
            status_text.text("🎙️ Generating audio...")
            time.sleep(2)
            
            progress_bar.progress(100)
            status_text.text("✅ Conversion completed!")
        
        return result, None
        
    except ImportError as e:
        error_msg = f"❌ Import Error: {str(e)}. Please ensure all dependencies are installed."
        if show_progress:
            status_text.text(error_msg)
        return None, error_msg
    except AttributeError as e:
        error_msg = f"❌ Configuration Error: {str(e)}. Check tool instantiation and configuration files."
        if show_progress:
            status_text.text(error_msg)
        return None, error_msg
    except Exception as e:
        error_msg = f"❌ Error during conversion: {str(e)}"
        if show_progress:
            status_text.text(error_msg)
        return None, error_msg

def find_generated_files():
    """Find the most recently generated audio and script files"""
    audio_dir = Path("output/audio")
    scripts_dir = Path("output/scripts") 
    metadata_dir = Path("output/metadata")
    
    # Find all related audio files from the most recent session
    audio_files = []
    if audio_dir.exists():
        all_audio_files = list(audio_dir.glob("*.mp3"))
        if all_audio_files:
            # Get the most recent audio file to determine the session
            most_recent = max(all_audio_files, key=os.path.getctime)
            
            # Extract base name (without part number) to find all related files
            most_recent_name = most_recent.stem  # e.g., "code_and_culture_part4"
            
            # Check if this is a multi-part file
            if "_part" in most_recent_name:
                base_name = most_recent_name.rsplit("_part", 1)[0]  # e.g., "code_and_culture"
                
                # Find all parts of this session
                related_files = []
                for file in all_audio_files:
                    if file.stem.startswith(base_name + "_part"):
                        related_files.append(file)
                
                # Sort by part number
                audio_files = sorted(related_files, key=lambda x: x.stem)
            else:
                # Single file, not multi-part
                audio_files = [most_recent]
    
    # Find script file in new organized location
    script_file = scripts_dir / "podcast_script.txt"
    
    # Find info file in new organized location  
    info_file = metadata_dir / "podcast_audio_info.txt"
    
    return {
        'audio': audio_files,  # Now returns a list of files instead of single file
        'script': script_file if script_file.exists() else None,
        'info': info_file if info_file.exists() else None
    }

def display_results(files: dict):
    """Display the conversion results with audio player and downloads"""
    
    st.markdown("""
    <div class="success-card">
        <h2>🎉 Conversion Successful!</h2>
        <p>Your blog post has been transformed into a professional podcast episode</p>
        <p><small>💡 Tip: Downloads won't reset the page - you can download all files!</small></p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Audio player(s)
        if files['audio']:
            # Check if it's multiple parts or single file
            audio_files = files['audio'] if isinstance(files['audio'], list) else [files['audio']]
            
            if len(audio_files) > 1:
                st.markdown(f"### 🎵 Generated Podcast ({len(audio_files)} Parts)")
                st.info("📢 **Multi-Part Podcast**: Your content was split into multiple parts for optimal listening experience. Play them in order!")
                
                # Display each part
                for i, audio_file in enumerate(audio_files, 1):
                    with st.expander(f"🎧 Part {i}: {audio_file.name}", expanded=(i == 1)):
                        # Display audio player
                        with open(audio_file, 'rb') as f:
                            audio_bytes = f.read()
                        
                        st.audio(audio_bytes, format='audio/mp3')
                        
                        # File info
                        file_size = os.path.getsize(audio_file) / (1024 * 1024)  # MB
                        st.info(f"📁 File: {audio_file.name} | 📏 Size: {file_size:.2f} MB")
                        
                        # Download button for each part
                        st.download_button(
                            label=f"📥 Download Part {i}",
                            data=audio_bytes,
                            file_name=audio_file.name,
                            mime="audio/mp3",
                            key=f"download_part_{i}"
                        )
                
                # Calculate total size
                total_size = sum(os.path.getsize(f) for f in audio_files) / (1024 * 1024)
                st.success(f"📊 Total Podcast Length: {len(audio_files)} parts | Total Size: {total_size:.2f} MB")
                
            else:
                # Single file display (existing logic)
                st.markdown("### 🎵 Generated Podcast")
                audio_file = audio_files[0]
                
                # Display audio player
                with open(audio_file, 'rb') as f:
                    audio_bytes = f.read()
                
                st.audio(audio_bytes, format='audio/mp3')
                
                # File info
                file_size = os.path.getsize(audio_file) / (1024 * 1024)  # MB
                st.info(f"📁 File: {audio_file.name} | 📏 Size: {file_size:.2f} MB")
                
                # Download button
                st.download_button(
                    label="📥 Download MP3",
                    data=audio_bytes,
                    file_name=audio_file.name,
                    mime="audio/mp3"
                )
    
    with col2:
        # Stats and info
        st.markdown("""
        <div class="stats-container">
            <h4>📊 Generation Stats</h4>
            <p>✅ Professional Quality<br>
            🎯 Optimized for Podcasts<br>
            💰 Cost: ~$0.20</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Script preview
    if files['script']:
        with st.expander("📝 View Generated Script", expanded=False):
            try:
                with open(files['script'], 'r', encoding='utf-8') as f:
                    script_content = f.read()
                st.text_area("Podcast Script", script_content, height=300)
                
                # Download script
                st.download_button(
                    label="📄 Download Script",
                    data=script_content,
                    file_name="podcast_script.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Could not read script file: {e}")

def main():
    load_css()
    create_header()
    
    # Sidebar
    selected_voice, show_progress, auto_play = create_sidebar()
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["🎙️ Convert", "📚 Examples", "🔧 Settings"])
    
    with tab1:
        # URL input section
        st.markdown("## 📰 Enter Blog URL")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            blog_url = st.text_input(
                "Blog URL",
                placeholder="https://example.com/blog-post",
                help="Enter any blog or article URL to convert to podcast"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            convert_button = st.button("🚀 Convert to Podcast", type="primary")
        
        # Conversion process
        if convert_button and blog_url:
            if blog_url.startswith(('http://', 'https://')):
                st.markdown("---")
                
                with st.container():
                    result, error = run_conversion(blog_url, selected_voice, show_progress)
                    
                    if result:
                        # Increment counter
                        st.session_state.conversion_count += 1
                        
                        # Find and store generated files in session state
                        files = find_generated_files()
                        st.session_state.last_conversion_files = files
                        st.session_state.last_conversion_successful = True
                        
                        # Auto-play if enabled
                        if auto_play and files['audio']:
                            st.balloons()
                    
                    elif error:
                        st.session_state.last_conversion_successful = False
                        st.error(error)
                        st.info("💡 **Troubleshooting Tips:**\n"
                               "- Check if the URL is accessible\n"
                               "- Ensure your API keys are set in .env file\n"
                               "- Try a different blog URL")
            else:
                st.error("❌ Please enter a valid URL starting with http:// or https://")
        
        elif convert_button and not blog_url:
            st.warning("⚠️ Please enter a blog URL to convert")
        
        # Display results if we have a successful conversion in session state
        if st.session_state.get('last_conversion_successful', False) and st.session_state.get('last_conversion_files'):
            st.markdown("---")
            
            # Add clear results button
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("🗑️ Clear Results"):
                    st.session_state.last_conversion_successful = False
                    st.session_state.last_conversion_files = None
                    st.rerun()
            
            display_results(st.session_state.last_conversion_files)
        
        # Show features if no successful conversion yet
        if not st.session_state.get('last_conversion_successful', False):
            show_features()
    
    with tab2:
        st.markdown("## 📚 Examples & Use Cases")
        
        st.markdown("""
        ### 🎯 Perfect for Converting:
        
        **📰 News Articles**
        - Daily news summaries
        - Industry updates
        - Research findings
        
        **📖 Blog Posts** 
        - Technical tutorials
        - Opinion pieces
        - How-to guides
        
        **🏢 Business Content**
        - Company announcements  
        - Product updates
        - Thought leadership
        
        **📚 Educational Content**
        - Course materials
        - Research papers
        - Study guides
        """)
        
        st.markdown("### 🎵 Sample Outputs")
        st.info("🎧 Generated podcasts are typically 3-7 minutes long with professional narration quality")
    
    with tab3:
        st.markdown("## 🔧 Configuration")
        
        # API key status
        st.markdown("### 🔑 API Key Status")
        
        openai_key = os.getenv('OPENAI_API_KEY')
        firecrawl_key = os.getenv('FIRECRAWL_API_KEY')
        
        col1, col2 = st.columns(2)
        
        with col1:
            if openai_key:
                st.success("✅ OpenAI API Key: Configured")
            else:
                st.error("❌ OpenAI API Key: Missing")
        
        with col2:
            if firecrawl_key:
                st.success("✅ Firecrawl API Key: Configured")
            else:
                st.error("❌ Firecrawl API Key: Missing")
        
        if not openai_key or not firecrawl_key:
            st.warning("⚠️ Please set your API keys in the .env file to use the converter")
            
            st.code("""
# Add to your .env file:
OPENAI_API_KEY=your_openai_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
MODEL=gpt-4o
            """)
        
        # Output directory info
        st.markdown("### 📁 Output Directory Structure")
        
        # Check each directory
        directories = {
            "📄 Scripts": "output/scripts",
            "🎵 Audio Files": "output/audio", 
            "📊 Metadata": "output/metadata"
        }
        
        for label, path in directories.items():
            dir_path = Path(path)
            if dir_path.exists():
                if path.endswith("audio"):
                    files = list(dir_path.glob("*.mp3"))
                    st.info(f"{label}: {len(files)} files in `{path}/`")
                elif path.endswith("scripts"): 
                    files = list(dir_path.glob("*.txt"))
                    st.info(f"{label}: {len(files)} files in `{path}/`")
                else:
                    files = list(dir_path.glob("*.*"))
                    st.info(f"{label}: {len(files)} files in `{path}/`")
            else:
                st.info(f"{label}: `{path}/` (will be created on first use)")

if __name__ == "__main__":
    main()
