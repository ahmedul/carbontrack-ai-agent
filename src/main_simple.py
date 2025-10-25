"""
CarbonTrack AI Agent - Main Entry Point (Simplified)

Run the agent to promote CarbonTrack on LinkedIn.
Based on Grok's simplified architecture.
"""
import argparse
import json
import logging
from pathlib import Path

from agent import executor
from config import settings

# Setup logging
logging.basicConfig(
    level=settings.log_level.upper(),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main entry point for CarbonTrack AI Agent."""
    parser = argparse.ArgumentParser(
        description="CarbonTrack AI Agent - Automate LinkedIn promotion"
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Topic for the post or path to JSON input file"
    )
    parser.add_argument(
        "--topic",
        type=str,
        help="Topic to generate post about (alternative to --input)"
    )
    parser.add_argument(
        "--style",
        type=str,
        default="professional",
        choices=["professional", "casual", "enthusiastic", "technical"],
        help="Style of the post"
    )
    
    args = parser.parse_args()
    
    # Determine input
    input_text = None
    
    if args.input:
        # Check if it's a file path
        input_path = Path(args.input)
        if input_path.exists() and input_path.suffix == '.json':
            logger.info(f"Loading input from file: {args.input}")
            with open(input_path, 'r') as f:
                data = json.load(f)
                topic = data.get('topic', '')
                style = data.get('style', args.style)
                input_text = f"Generate a {style} LinkedIn post about {topic}"
        else:
            input_text = args.input
    elif args.topic:
        input_text = f"Generate a {args.style} LinkedIn post about {args.topic}"
    else:
        # Default example
        input_text = "Generate a professional LinkedIn post about CarbonTrack's carbon tracking features"
        logger.info("No input provided, using default example")
    
    logger.info(f"Running agent with input: {input_text}")
    
    try:
        # Run the agent
        result = executor.invoke({"input": input_text})
        
        print("\n" + "="*60)
        print("AGENT EXECUTION RESULT")
        print("="*60)
        print(result)
        print("="*60 + "\n")
        
        logger.info("Agent execution completed successfully")
        
    except Exception as e:
        logger.error(f"Error running agent: {e}", exc_info=True)
        print(f"\n❌ Error: {e}\n")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
