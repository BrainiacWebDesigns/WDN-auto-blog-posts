#!/usr/bin/env bash
cd /home/a2c11527_admin/WDN-auto-blog-posts
git pull origin main
python3 update_topics.py

# Generate first blog post
./generate_blog.sh

# Generate second blog post
./generate_blog.sh
