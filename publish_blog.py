import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# When executed directly, this script reads ``blog_post.txt`` and
# publishes its contents to WordPress. The first line of the file is
# treated as the post title and the remainder as the body.

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

# When run as a script, publish the contents of blog_post.txt.
# The first line becomes the post title and the remainder is the body.
if __name__ == "__main__":
    try:
        with open("blog_post.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        if not lines:
            raise ValueError("blog_post.txt is empty")
        title = lines[0]
        content = "\n".join(lines[1:]).strip() or title
    except FileNotFoundError:
        print("❌ blog_post.txt not found. Generate a post first.")
        raise SystemExit(1)
    except Exception as e:
        print(f"❌ Error reading blog_post.txt: {e}")
        raise SystemExit(1)

    publish_blog_post(title, content)
