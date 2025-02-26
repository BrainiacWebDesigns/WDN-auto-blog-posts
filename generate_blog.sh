#!/usr/bin/env bash

cd /mnt/c/Users/doug/WDN-auto-blog-posts
git pull origin main

# Pick a random topic from topics.txt
TOPIC=$(shuf -n 1 topics.txt)

# Generate a ~1000-word post with GPT-4
python3 generate_ai_post.py "$TOPIC"

# Publish to WordPress
python3 publish_blog.py
