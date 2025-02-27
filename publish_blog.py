#!/usr/bin/env python3
import os
import requests

# Load WordPress API credentials from environment variables.
WP_URL = os.getenv("WP_URL", "https://www.webdesignnerd.com/wp-json/wp/v2")
WP_USERNAME = os.getenv("a2c11527_admin")
WP_PASSWORD = os.getenv("dgJk anmN SJb5 VyNI VCJM Jyg6")

def publish_blog():
    # Read the generated blog content from the current directory.
    try:
        with open("blog_post.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ blog_post.txt not found in the current directory.")
        return

    # Prepare the post data.
    data = {
        "title": "Test Post: Automated Blog Post",
        "content": content,
        "status": "publish"  # Use "draft" if you prefer to review before publishing.
    }
    
    # Make the POST request to the WordPress REST API.
    response = requests.post(
        f"{WP_URL}/posts",
        json=data,
        auth=(WP_USERNAME, WP_PASSWORD)
    )
    
    if response.status_code == 201:
        print("✅ Post published successfully!")
        print("Post URL:", response.json().get("link"))
    else:
        print("❌ Failed to publish post.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    publish_blog()