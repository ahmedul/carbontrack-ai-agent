"""
Post to LinkedIn Tool - Publishes content to LinkedIn
"""
from typing import Optional, Type
from langchain_core.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field
from pathlib import Path
import requests
import json

import sys
sys.path.append(str(Path(__file__).parent.parent))

from config import settings
import logging

logger = logging.getLogger(__name__)


class PostToLinkedInInput(BaseModel):
    """Input schema for the PostToLinkedIn tool."""
    post_text: str = Field(description="The text content of the LinkedIn post")
    video_path: str = Field(
        description="Path to the video file to attach (optional)",
        default=""
    )
    image_path: str = Field(
        description="Path to an image file to attach (optional)",
        default=""
    )


class PostToLinkedInTool(BaseTool):
    """
    LangChain tool that posts content to LinkedIn.
    
    This tool publishes text posts with optional video or image attachments
    to LinkedIn using the LinkedIn API.
    """
    
    name: str = "post_to_linkedin"
    description: str = """
    Post content to LinkedIn.
    Input should include post_text, and optionally video_path or image_path.
    Returns confirmation of the post or error message.
    """
    args_schema: Type[BaseModel] = PostToLinkedInInput
    
    def _run(
        self,
        post_text: str,
        video_path: str = "",
        image_path: str = "",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Post content to LinkedIn."""
        logger.info("Preparing to post to LinkedIn")
        
        # Check if auto-posting is enabled
        if not settings.auto_post:
            logger.info("Auto-post is disabled. Content prepared but not posted.")
            return self._preview_post(post_text, video_path, image_path)
        
        # Validate credentials
        if not settings.linkedin_access_token or not settings.linkedin_user_id:
            error_msg = "LinkedIn credentials not configured. Please set LINKEDIN_ACCESS_TOKEN and LINKEDIN_USER_ID."
            logger.error(error_msg)
            return f"Error: {error_msg}"
        
        try:
            # Post to LinkedIn
            if video_path:
                return self._post_with_video(post_text, video_path)
            elif image_path:
                return self._post_with_image(post_text, image_path)
            else:
                return self._post_text_only(post_text)
            
        except Exception as e:
            logger.error(f"Error posting to LinkedIn: {e}")
            return f"Error posting to LinkedIn: {str(e)}"
    
    def _preview_post(self, post_text: str, video_path: str, image_path: str) -> str:
        """Create a preview of the post without actually posting."""
        preview = f"""
📝 LinkedIn Post Preview
========================

{post_text}

Attachments:
- Video: {video_path if video_path else 'None'}
- Image: {image_path if image_path else 'None'}

Status: Ready to post (auto_post is disabled)
To enable auto-posting, set AUTO_POST=true in .env

========================
"""
        print(preview)
        return "Post prepared successfully. Preview shown above."
    
    def _post_text_only(self, post_text: str) -> str:
        """Post text-only content to LinkedIn."""
        logger.info("Posting text-only to LinkedIn")
        
        url = "https://api.linkedin.com/v2/ugcPosts"
        headers = {
            "Authorization": f"Bearer {settings.linkedin_access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
        
        payload = {
            "author": f"urn:li:person:{settings.linkedin_user_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_text
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 201:
            post_id = response.json().get("id")
            logger.info(f"Post published successfully: {post_id}")
            return f"✅ Post published successfully! Post ID: {post_id}"
        else:
            error_msg = f"Failed to post: {response.status_code} - {response.text}"
            logger.error(error_msg)
            return f"Error: {error_msg}"
    
    def _post_with_image(self, post_text: str, image_path: str) -> str:
        """Post with an image attachment."""
        logger.info(f"Posting with image: {image_path}")
        
        # First, upload the image
        image_urn = self._upload_image(image_path)
        if not image_urn:
            return "Error: Failed to upload image"
        
        url = "https://api.linkedin.com/v2/ugcPosts"
        headers = {
            "Authorization": f"Bearer {settings.linkedin_access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
        
        payload = {
            "author": f"urn:li:person:{settings.linkedin_user_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_text
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "media": image_urn
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 201:
            post_id = response.json().get("id")
            logger.info(f"Post with image published successfully: {post_id}")
            return f"✅ Post with image published successfully! Post ID: {post_id}"
        else:
            error_msg = f"Failed to post: {response.status_code} - {response.text}"
            logger.error(error_msg)
            return f"Error: {error_msg}"
    
    def _post_with_video(self, post_text: str, video_path: str) -> str:
        """Post with a video attachment."""
        logger.info(f"Posting with video: {video_path}")
        
        # Note: Video posting to LinkedIn is more complex and requires:
        # 1. Registering the upload
        # 2. Uploading the video in chunks
        # 3. Finalizing the upload
        # 4. Creating the post with the video URN
        
        # For now, provide a simplified implementation
        logger.warning("Video posting is a complex multi-step process")
        
        return """
⚠️ Video posting requires additional setup.

LinkedIn video posts require:
1. Registering video upload
2. Chunked upload process
3. Video processing time

For now, please:
1. Upload the video manually from: {video_path}
2. Or use the text-only post and add video later

Future versions will support automated video posting.
""".format(video_path=video_path)
    
    def _upload_image(self, image_path: str) -> Optional[str]:
        """Upload an image to LinkedIn and return the asset URN."""
        try:
            # Step 1: Register upload
            register_url = "https://api.linkedin.com/v2/assets?action=registerUpload"
            headers = {
                "Authorization": f"Bearer {settings.linkedin_access_token}",
                "Content-Type": "application/json"
            }
            
            register_payload = {
                "registerUploadRequest": {
                    "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
                    "owner": f"urn:li:person:{settings.linkedin_user_id}",
                    "serviceRelationships": [
                        {
                            "relationshipType": "OWNER",
                            "identifier": "urn:li:userGeneratedContent"
                        }
                    ]
                }
            }
            
            response = requests.post(register_url, headers=headers, json=register_payload)
            
            if response.status_code != 200:
                logger.error(f"Failed to register upload: {response.text}")
                return None
            
            upload_info = response.json()
            upload_url = upload_info["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
            asset_urn = upload_info["value"]["asset"]
            
            # Step 2: Upload the image
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            upload_headers = {
                "Authorization": f"Bearer {settings.linkedin_access_token}",
            }
            
            upload_response = requests.put(upload_url, headers=upload_headers, data=image_data)
            
            if upload_response.status_code != 201:
                logger.error(f"Failed to upload image: {upload_response.text}")
                return None
            
            logger.info(f"Image uploaded successfully: {asset_urn}")
            return asset_urn
            
        except Exception as e:
            logger.error(f"Error uploading image: {e}")
            return None
    
    async def _arun(
        self,
        post_text: str,
        video_path: str = "",
        image_path: str = "",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Async version - for now just calls sync version."""
        return self._run(
            post_text=post_text,
            video_path=video_path,
            image_path=image_path,
            run_manager=run_manager,
        )


# Example usage
if __name__ == "__main__":
    tool = PostToLinkedInTool()
    result = tool._run(
        post_text="Excited to share my new project! 🚀 #innovation #tech",
        video_path="",
        image_path=""
    )
    print(result)
