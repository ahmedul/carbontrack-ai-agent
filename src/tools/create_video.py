"""
Create Video Tool - Records website demos using Playwright
"""
from typing import Optional, Type
from langchain_core.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field
from playwright.sync_api import sync_playwright
from pathlib import Path
import time

import sys
sys.path.append(str(Path(__file__).parent.parent))

from config import settings, get_video_dimensions, OUTPUT_DIR
import logging

logger = logging.getLogger(__name__)


class CreateVideoInput(BaseModel):
    """Input schema for the CreateVideo tool."""
    website_url: str = Field(description="URL of the website to record")
    duration: int = Field(
        description="Duration of the video in seconds",
        default=30
    )
    output_filename: str = Field(
        description="Name of the output video file (without extension)",
        default="demo"
    )


class CreateVideoTool(BaseTool):
    """
    LangChain tool that creates demo videos of websites using Playwright.
    
    This tool opens a website in a browser, scrolls through it,
    and records the screen to create a demo video.
    """
    
    name: str = "create_video"
    description: str = """
    Create a demo video of a website.
    Input should include website_url, and optionally duration (in seconds) 
    and output_filename.
    Returns the path to the created video file.
    """
    args_schema: Type[BaseModel] = CreateVideoInput
    
    def _run(
        self,
        website_url: str,
        duration: int = 30,
        output_filename: str = "demo",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Create a demo video of the website."""
        logger.info(f"Creating {duration}s video of: {website_url}")
        
        try:
            # Get video settings
            width, height = get_video_dimensions()
            output_path = OUTPUT_DIR / f"{output_filename}.{settings.video_format}"
            
            with sync_playwright() as p:
                # Launch browser
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    record_video_dir=str(OUTPUT_DIR),
                    record_video_size={"width": width, "height": height}
                )
                page = context.new_page()
                
                logger.info(f"Loading website: {website_url}")
                page.goto(website_url, wait_until="networkidle")
                
                # Scroll through the page slowly
                start_time = time.time()
                scroll_position = 0
                page_height = page.evaluate("document.body.scrollHeight")
                scroll_step = page_height / (duration * 2)  # Scroll speed
                
                logger.info("Recording video...")
                while (time.time() - start_time) < duration:
                    scroll_position += scroll_step
                    page.evaluate(f"window.scrollTo(0, {scroll_position})")
                    time.sleep(0.5)
                    
                    # Reset scroll if we reach the bottom
                    if scroll_position >= page_height:
                        scroll_position = 0
                
                # Close browser and save video
                logger.info("Finalizing video...")
                context.close()
                browser.close()
            
            # The video is saved with a generated name, we need to rename it
            video_files = list(OUTPUT_DIR.glob("*.webm"))
            if video_files:
                latest_video = max(video_files, key=lambda p: p.stat().st_mtime)
                
                # Convert webm to desired format if needed
                if settings.video_format != "webm":
                    self._convert_video(latest_video, output_path)
                    latest_video.unlink()  # Remove original webm
                else:
                    latest_video.rename(output_path)
                
                logger.info(f"Video created successfully: {output_path}")
                return str(output_path)
            else:
                error_msg = "No video file was created"
                logger.error(error_msg)
                return f"Error: {error_msg}"
            
        except Exception as e:
            logger.error(f"Error creating video: {e}")
            return f"Error creating video: {str(e)}"
    
    def _convert_video(self, input_path: Path, output_path: Path):
        """Convert video format using opencv if needed."""
        try:
            import cv2
            
            logger.info(f"Converting video from {input_path.suffix} to {output_path.suffix}")
            
            # Read the video
            cap = cv2.VideoCapture(str(input_path))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            # Define codec and create VideoWriter
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)
            
            cap.release()
            out.release()
            logger.info("Video conversion complete")
            
        except ImportError:
            logger.warning("OpenCV not available, keeping webm format")
            input_path.rename(output_path.with_suffix('.webm'))
        except Exception as e:
            logger.error(f"Error converting video: {e}")
            # Fallback: just rename to .webm
            input_path.rename(output_path.with_suffix('.webm'))
    
    async def _arun(
        self,
        website_url: str,
        duration: int = 30,
        output_filename: str = "demo",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Async version - for now just calls sync version."""
        return self._run(
            website_url=website_url,
            duration=duration,
            output_filename=output_filename,
            run_manager=run_manager,
        )


# Example usage
if __name__ == "__main__":
    tool = CreateVideoTool()
    result = tool._run(
        website_url="https://github.com",
        duration=10,
        output_filename="github_demo"
    )
    print(f"Video created: {result}")
