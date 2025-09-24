#!/usr/bin/env python
import sys
import warnings
import argparse

from datetime import datetime

from blog_to_podcast.crew import BlogToPodcast

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with user input for blog URL.
    """
    # Get blog URL from user input
    blog_url = input("Enter the blog URL to convert to podcast: ").strip()
    
    if not blog_url:
        raise ValueError("Blog URL is required!")
    
    # Get optional voice selection
    print("\nAvailable voices: alloy, echo, fable, onyx, nova, shimmer")
    voice = input("Select voice (default: alloy): ").strip().lower()
    if voice not in ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']:
        voice = 'alloy'
    
    inputs = {
        'blog_url': blog_url,
        'voice': voice,
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = BlogToPodcast().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        BlogToPodcast().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BlogToPodcast().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        BlogToPodcast().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_cli(blog_url: str, voice: str = "alloy"):
    """
    Run blog-to-podcast conversion via CLI.
    
    Args:
        blog_url: The URL of the blog post to convert
        voice: Voice to use for TTS (default: alloy)
    """
    inputs = {
        'blog_url': blog_url,
        'voice': voice,
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = BlogToPodcast().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def main():
    """Main entry point for CLI usage."""
    parser = argparse.ArgumentParser(
        description="Convert blog posts to podcasts using AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m blog_to_podcast.main --url https://example.com/blog-post
  python -m blog_to_podcast.main --url https://example.com/blog-post --voice nova
        """
    )
    
    parser.add_argument(
        "--url", 
        required=True, 
        help="URL of the blog post to convert to podcast"
    )
    
    parser.add_argument(
        "--voice", 
        choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'],
        default='alloy',
        help="Voice to use for text-to-speech (default: alloy)"
    )
    
    args = parser.parse_args()
    
    try:
        run_cli(args.url, args.voice)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    main()
