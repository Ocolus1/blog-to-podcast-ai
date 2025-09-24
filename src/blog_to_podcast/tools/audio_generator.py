from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import openai
import os
import hashlib
import datetime


class AudioGeneratorInput(BaseModel):
    """Input schema for AudioGenerator."""
    podcast_script: str = Field(..., description="The podcast script to convert to audio.")
    voice: str = Field(default="alloy", description="Voice to use: alloy, echo, fable, onyx, nova, shimmer")
    output_filename: str = Field(default="", description="Optional custom filename for the audio file")


class AudioGenerator(BaseTool):
    name: str = "Audio Generator"
    description: str = (
        "Converts podcast script to high-quality audio using OpenAI's Text-to-Speech API. "
        "Supports multiple voices and generates MP3 files ready for podcast distribution."
    )
    args_schema: Type[BaseModel] = AudioGeneratorInput

    def _run(self, podcast_script: str, voice: str = "alloy", output_filename: str = "") -> str:
        """
        Convert podcast script to audio using OpenAI TTS.
        
        Args:
            podcast_script: The text script to convert to audio
            voice: Voice selection (alloy, echo, fable, onyx, nova, shimmer)
            output_filename: Optional custom filename
            
        Returns:
            Path to the generated audio file or error message
        """
        try:
            # Get API key from environment
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                return "Error: OPENAI_API_KEY not found in environment variables."
            
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=api_key)
            
            # Validate voice selection
            valid_voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
            if voice not in valid_voices:
                voice = "alloy"  # Default fallback
            
            # Clean the script for TTS (remove metadata headers)
            lines = podcast_script.split('\n')
            clean_script = []
            skip_metadata = False
            
            for line in lines:
                line = line.strip()
                if line.startswith("PODCAST SCRIPT GENERATED") or line.startswith("---"):
                    skip_metadata = True
                    continue
                if skip_metadata and line and not line.startswith("Script generated"):
                    skip_metadata = False
                if not skip_metadata and line:
                    clean_script.append(line)
            
            final_script = '\n'.join(clean_script).strip()
            
            if not final_script:
                return "Error: No valid script content found for audio generation."
            
            # Generate filename if not provided
            if not output_filename:
                # Create hash-based filename with timestamp
                script_hash = hashlib.md5(final_script.encode()).hexdigest()[:8]
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                output_filename = f"podcast_{timestamp}_{script_hash}.mp3"
            
            # Ensure filename has .mp3 extension
            if not output_filename.endswith('.mp3'):
                output_filename += '.mp3'
            
            # Create output directories if they don't exist
            output_dir = os.path.join(os.getcwd(), "output", "audio")
            metadata_dir = os.path.join(os.getcwd(), "output", "metadata")
            scripts_dir = os.path.join(os.getcwd(), "output", "scripts")
            
            os.makedirs(output_dir, exist_ok=True)
            os.makedirs(metadata_dir, exist_ok=True)
            os.makedirs(scripts_dir, exist_ok=True)
            
            output_path = os.path.join(output_dir, output_filename)
            
            # Generate audio using OpenAI TTS
            response = client.audio.speech.create(
                model="tts-1",  # Using standard quality for cost efficiency
                voice=voice,
                input=final_script,
                response_format="mp3"
            )
            
            # Save the audio file
            with open(output_path, 'wb') as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
            
            # Calculate approximate cost (OpenAI TTS: $0.015 per 1K characters)
            char_count = len(final_script)
            estimated_cost = (char_count / 1000) * 0.015
            
            # Get file size
            file_size = os.path.getsize(output_path)
            file_size_mb = file_size / (1024 * 1024)
            
            success_message = f"""
Audio generation completed successfully!

Details:
- Output file: {output_path}
- Voice used: {voice}
- File size: {file_size_mb:.2f} MB
- Script length: {char_count:,} characters
- Estimated cost: ${estimated_cost:.4f}

The audio file is ready for podcast distribution.
"""
            return success_message.strip()
                
        except openai.AuthenticationError:
            return "Error: Invalid OpenAI API key. Please check your OPENAI_API_KEY environment variable."
        except openai.RateLimitError:
            return "Error: OpenAI API rate limit exceeded. Please try again later."
        except openai.APIError as e:
            return f"Error: OpenAI API error during audio generation: {str(e)}"
        except PermissionError:
            return f"Error: Permission denied when writing to output directory. Please check file permissions."
        except Exception as e:
            return f"Error: Unexpected error during audio generation: {str(e)}"
