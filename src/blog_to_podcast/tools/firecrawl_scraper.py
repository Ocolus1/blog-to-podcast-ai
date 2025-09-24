from crewai.tools import BaseTool
from typing import Type, Dict, Any
from pydantic import BaseModel, Field
import requests
import os
from urllib.parse import urlparse


class FirecrawlScraperInput(BaseModel):
    """Input schema for FirecrawlScraper."""
    url: str = Field(..., description="The URL of the blog post to scrape.")


class FirecrawlScraper(BaseTool):
    name: str = "Firecrawl Blog Scraper"
    description: str = (
        "Scrapes blog content from any URL using Firecrawl API. "
        "Returns clean, structured text content suitable for processing."
    )
    args_schema: Type[BaseModel] = FirecrawlScraperInput

    def _run(self, url: str) -> str:
        """
        Scrape blog content using Firecrawl API.
        
        Args:
            url: The URL of the blog post to scrape
            
        Returns:
            Cleaned text content of the blog post
        """
        try:
            # Get API key from environment
            api_key = os.getenv('FIRECRAWL_API_KEY')
            if not api_key:
                return "Error: FIRECRAWL_API_KEY not found in environment variables."
            
            # Validate URL
            parsed_url = urlparse(url)
            if not parsed_url.scheme or not parsed_url.netloc:
                return f"Error: Invalid URL format: {url}"
            
            # Use Firecrawl Python SDK
            from firecrawl import FirecrawlApp
            
            app = FirecrawlApp(api_key=api_key)
            
            # Use the correct method name 'scrape' instead of 'scrape_url'
            result = app.scrape(url, formats=["markdown"])
            
            # The result is a Document object, not a dict
            if result:
                # Access attributes directly from the Document object
                title = getattr(result, 'title', 'Unknown Title') or 'Unknown Title'
                content = getattr(result, 'markdown', '') or getattr(result, 'content', '')
                
                # Try to get metadata if available
                metadata = getattr(result, 'metadata', {}) or {}
                author = metadata.get('author', 'Unknown Author') if isinstance(metadata, dict) else 'Unknown Author'
                
                # Format the extracted content
                formatted_content = f"""
BLOG POST CONTENT:

Title: {title}
Author: {author}
URL: {url}

Content:
{content}
"""
                return formatted_content.strip()
            else:
                return f"Error: No content found in Firecrawl response for URL: {url}"
                
        except requests.exceptions.Timeout:
            return f"Error: Request timeout while scraping {url}"
        except requests.exceptions.RequestException as e:
            return f"Error: Network error while scraping {url}: {str(e)}"
        except Exception as e:
            return f"Error: Unexpected error while scraping {url}: {str(e)}"
