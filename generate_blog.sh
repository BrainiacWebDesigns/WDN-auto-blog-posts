#!/bin/bash

# Navigate to GitHub repository directory
cd "C:\Users\doug\WDN-auto-blog-posts"

# Pull the latest updates from GitHub
git pull origin main

# Select a random topic from topics.txt
TOPIC=$(shuf -n 1 topics.txt)

# Create a prompt with the selected topic
echo "Write a 1000-word SEO-optimized blog post about \"$TOPIC\".
Include:
- Keyword-optimized title
- Meta title & description
- SEO-friendly slug
- Internal & external links
- Call-to-action to visit www.webdesignnerd.com" > prompt.txt

# Run Llama 3 to generate the blog post
ollama run llama3 < prompt.txt > blog_post.txt

# Publish the blog post
python publish_blog.py