"""
CarbonTrack AI Agent - Main Entry Point

This is the main script to run the CarbonTrack Promoter AI agent.
"""
import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict, Any

from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich import print as rprint

# Add src to path
sys.path.append(str(Path(__file__).parent))

from config import settings
from agent import create_carbontrack_agent
from tools import GeneratePostTool, CreateVideoTool, PostToLinkedInTool

# Setup logging
console = Console()
logging.basicConfig(
    level=settings.log_level,
    format="%(message)s",
    handlers=[
        RichHandler(console=console, rich_tracebacks=True),
        logging.FileHandler(settings.log_file)
    ]
)
logger = logging.getLogger(__name__)


def load_input_from_file(file_path: str) -> Dict[str, Any]:
    """Load input data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        logger.info(f"Loaded input from: {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading input file: {e}")
        sys.exit(1)


def load_input_interactive() -> Dict[str, Any]:
    """Interactively prompt user for input."""
    console.print("\n[bold cyan]CarbonTrack Promoter - Interactive Mode[/bold cyan]\n")
    
    project_name = console.input("[yellow]Project Name:[/yellow] ")
    website_url = console.input("[yellow]Website URL:[/yellow] ")
    description = console.input("[yellow]Description:[/yellow] ")
    
    console.print("\n[yellow]Key Features (one per line, empty line to finish):[/yellow]")
    key_features = []
    while True:
        feature = console.input("  - ")
        if not feature:
            break
        key_features.append(feature)
    
    tone = console.input(
        "[yellow]Post Tone (professional/casual/enthusiastic/technical):[/yellow] ",
    ) or "professional"
    
    return {
        "project_name": project_name,
        "website_url": website_url,
        "description": description,
        "key_features": key_features,
        "tone": tone
    }


def display_welcome():
    """Display welcome message."""
    welcome_text = """
[bold green]🌱 CarbonTrack Promoter AI Agent[/bold green]

An open-source AI agent that promotes your projects on LinkedIn.

Features:
  🤖 AI-powered post generation
  🎥 Automated demo videos
  📱 LinkedIn publishing

LLM Provider: [cyan]{llm_provider}[/cyan]
Auto-post: [cyan]{auto_post}[/cyan]
""".format(
        llm_provider=settings.llm_provider,
        auto_post="Enabled" if settings.auto_post else "Disabled"
    )
    
    console.print(Panel(welcome_text, border_style="green"))


def main():
    """Main entry point for the CarbonTrack agent."""
    parser = argparse.ArgumentParser(
        description="CarbonTrack Promoter - AI Agent for LinkedIn Promotion"
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        help="Path to input JSON file with project details"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode (prompt for input)"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Display welcome message
    display_welcome()
    
    # Load input data
    if args.input:
        input_data = load_input_from_file(args.input)
    elif args.interactive:
        input_data = load_input_interactive()
    else:
        # Default: use example input
        console.print("\n[yellow]No input provided. Using example data...[/yellow]\n")
        input_data = {
            "project_name": "CarbonTrack",
            "website_url": "https://github.com",
            "description": "A sustainability tracking app that helps users reduce their carbon footprint",
            "key_features": [
                "Carbon footprint tracking",
                "AI-powered recommendations",
                "Community challenges"
            ],
            "tone": "professional"
        }
    
    try:
        # Initialize tools
        console.print("\n[cyan]Initializing tools...[/cyan]")
        tools = [
            GeneratePostTool(),
            CreateVideoTool(),
            PostToLinkedInTool()
        ]
        
        # Create agent
        console.print("[cyan]Creating CarbonTrack agent...[/cyan]")
        agent = create_carbontrack_agent(tools)
        
        # Run agent
        console.print("\n[bold green]Running agent...[/bold green]\n")
        result = agent.run(input_data)
        
        # Display results
        console.print("\n[bold green]✅ Agent execution completed![/bold green]\n")
        console.print(Panel(
            f"[cyan]Output:[/cyan]\n{result.get('output', 'No output')}",
            title="Results",
            border_style="green"
        ))
        
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        logger.exception("Error running agent")
        console.print(f"\n[bold red]❌ Error: {e}[/bold red]\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
