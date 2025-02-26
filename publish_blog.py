#!/usr/bin/env python3
import os
import requests
import re

def process_images(text):
    """
    Replaces image placeholders of the form [Image: "filename.jpg"] with HTML <img> tags.
    Adjust the image base URL as needed.
    """
    pattern = r'\[Image:\s*"(.*?)"\]'
    replacement = r'<img src="https://www.webdesignnerd.com/images/\1" alt="Image related to the article">'
    return re.sub(pattern, replacement, text)

def main():
    # Set the local project directory (using WSL path format)
    script_dir = "/mnt/c/Users/doug/WDN-auto-blog-posts"
    blog_post_file = os.path.join(script_dir, "blog_post.txt")

    # Update these with your actual WordPress credentials
    WP_URL = "https://www.webdesignnerd.com/wp-json/wp/v2/posts"
    WP_USER = "a2c11527_admin"        # Replace with your WordPress username
    WP_APP_PASSWORD = "dgJk anmN SJb5 VyNI VCJM Jyg6"  # Replace with your WordPress Application Password

    # Read the generated blog post content
    try:
        with open(blog_post_file, "r", encoding="utf-8") as file:
            blog_content = file.read()
    except FileNotFoundError:
        print("❌ Error: blog_post.txt not found in", script_dir)
        return

    # Process image placeholders to convert them to HTML <img> tags
    blog_content = process_images(blog_content)

    # Extract title from the first line; the rest is considered the body
    lines = blog_content.splitlines()
    if not lines or not lines[0]:
        print("❌ Error: The blog post content is empty or missing a title.")
        return
    title = lines[0]

    # Generate an SEO-friendly slug (lowercase, hyphen-separated, no punctuation)
    slug = title.lower().replace(" ", "-").replace(",", "").replace("'", "")
    
    # Create a meta description from the first 150 characters of the content
    meta_description = blog_content[:150] + "..."

    # Build the payload for the WordPress REST API
    post_data = {
        "title": title,
        "content": blog_content,
        "status": "publish",  # Change to "draft" if you want to review before publishing
        "slug": slug,
        "meta": {
            "title": title,
            "description": meta_description
        },
        "categories": [71],  # Replace with the appropriate category ID if needed
    }

    # Post the blog content to WordPress
    response = requests.post(WP_URL, json=post_data, auth=(WP_USER, WP_APP_PASSWORD))

    if response.status_code == 201:
        print("✅ Blog post published successfully!")
    else:
        print("❌ Error publishing post:", response.status_code, response.text)

if __name__ == "__main__":
    main()
