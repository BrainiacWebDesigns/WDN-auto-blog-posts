import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve WordPress credentials from .env
WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_PASSWORD = os.getenv("WP_PASSWORD")

# Function to publish a blog post
def publish_blog_post(title, content):
    """Publishes a blog post to WordPress."""
    post_data = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    response = requests.post(
        f"{WP_URL}/posts",
        auth=(WP_USERNAME, WP_PASSWORD),
        headers={"Content-Type": "application/json"},
        json=post_data
    )

    if response.status_code == 201:
        post_info = response.json()
        print(f"✅ Post published successfully!")
        print(f"Post URL: {post_info.get('link', 'Unknown')}")
    else:
        print(f"❌ Failed to publish post. HTTP {response.status_code}")
        print(f"Response: {response.text}")

# Example usage (modify or integrate with your automation)
if __name__ == "__main__":
    test_title = "Test Post"
    test_content = "This is a test post generated by the automation script."
    publish_blog_post(test_title, test_content)
