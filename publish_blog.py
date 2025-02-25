import requests
import os

# Define the correct GitHub-based working directory
script_dir = "C:\\Users\\doug\\WDN-auto-blog-posts"
blog_post_file = os.path.join(script_dir, "blog_post.txt")

# WordPress API Credentials
WP_URL = "https://www.webdesignnerd.com/wp-json/wp/v2/posts"
WP_USER = "your_username"
WP_APP_PASSWORD = "your_application_password"

# Read the generated blog post
with open(blog_post_file, "r", encoding="utf-8") as file:
    blog_content = file.read()

# Extract the first line as the blog title
title = blog_content.split("\n")[0]

# Generate an SEO-friendly slug
slug = title.lower().replace(" ", "-").replace(",", "").replace("'", "")

# Meta description (first 150 chars of post)
meta_description = blog_content[:150] + "..."

# Set up WordPress post data
post_data = {
    "title": title,
    "content": blog_content,
    "status": "publish",
    "slug": slug,
    "meta": {
        "title": title,
        "description": meta_description
    },
    "categories": [1],  # Replace with actual category ID
}

# Send post request to WordPress
response = requests.post(WP_URL, json=post_data, auth=(WP_USER, WP_APP_PASSWORD))

if response.status_code == 201:
    print("✅ Blog post published successfully!")
else:
    print("❌ Error:", response.text)