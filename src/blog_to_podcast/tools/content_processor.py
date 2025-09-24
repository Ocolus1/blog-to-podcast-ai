from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import openai
import os
import json


class ContentProcessorInput(BaseModel):
    """Input schema for ContentProcessor."""
    blog_content: str = Field(..., description="The scraped blog content to process into podcast script.")


class ContentProcessor(BaseTool):
    name: str = "Content Processor"
    description: str = (
        "Processes blog content into a well-structured podcast script using OpenAI GPT-4. "
        "Creates engaging, conversational content suitable for text-to-speech conversion."
    )
    args_schema: Type[BaseModel] = ContentProcessorInput

    def _run(self, blog_content: str) -> str:
        """
        Process blog content into podcast script using OpenAI GPT-4.
        
        Args:
            blog_content: The scraped blog content
            
        Returns:
            Formatted podcast script ready for audio generation
        """
        try:
            # Get API key from environment
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                return "Error: OPENAI_API_KEY not found in environment variables."
            
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=api_key)
            
            # Create the prompt for podcast script generation
            system_prompt = """
You are an expert podcast script writer. Your task is to transform blog content into an engaging, conversational podcast script that sounds natural when read aloud.

Guidelines:
1. Create a compelling introduction that hooks the listener
2. Structure the content in a logical flow with smooth transitions
3. Use conversational language that sounds natural in audio format
4. Include brief pauses and emphasis markers for better speech synthesis
5. Add engaging elements like rhetorical questions and listener engagement
6. Keep sentences at moderate length for clear speech
7. Include a memorable conclusion with key takeaways
8. Format the script clearly with sections and speaker notes

The script should be approximately 3-7 minutes when read aloud (roughly 450-1050 words).
"""
            
            user_prompt = f"""
Transform the following blog content into an engaging podcast script:

{blog_content}

Create a podcast script that:
- Has a catchy introduction
- Presents the main points in an engaging, conversational way
- Includes natural transitions between topics
- Ends with a strong conclusion and call-to-action
- Is optimized for text-to-speech synthesis

Format the output as a clean script without any markdown formatting.
"""
            
            # Make API call to OpenAI
            response = client.chat.completions.create(
                model="gpt-4o",  # Using the model specified in .env
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            
            # Extract the generated script
            if response.choices and len(response.choices) > 0:
                podcast_script = response.choices[0].message.content
                
                # Add metadata header
                formatted_script = f"""
PODCAST SCRIPT GENERATED FROM BLOG CONTENT

{podcast_script}

---
Script generated using OpenAI GPT-4o
Ready for text-to-speech conversion
"""
                return formatted_script.strip()
            else:
                return "Error: No response generated from OpenAI API."
                
        except openai.AuthenticationError:
            return "Error: Invalid OpenAI API key. Please check your OPENAI_API_KEY environment variable."
        except openai.RateLimitError:
            return "Error: OpenAI API rate limit exceeded. Please try again later."
        except openai.APIError as e:
            return f"Error: OpenAI API error: {str(e)}"
        except Exception as e:
            return f"Error: Unexpected error during content processing: {str(e)}"
