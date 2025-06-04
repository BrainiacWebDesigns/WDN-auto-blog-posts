#!/usr/bin/env bash
# Change to the directory of the script (ensures we're in the right folder)
cd "$(dirname "$0")"

echo "Pulling latest changes from GitHub..."
git pull origin main

echo "Updating topics..."
python3 update_topics.py

# Choose a random topic from topics.txt
if [ -s topics.txt ]; then
    topic1=$(shuf -n 1 topics.txt)
else
    topic1="Default Topic"
fi

echo "Generating first blog post for topic: $topic1"
python3 generate_ai_post.py "$topic1"

echo "Publishing first blog post..."
python3 publish_blog.py

# For a second post, choose another random topic
if [ -s topics.txt ]; then
    topic2=$(shuf -n 1 topics.txt)
else
    topic2="Default Topic"
fi

echo "Generating second blog post for topic: $topic2"
python3 generate_ai_post.py "$topic2"

echo "Publishing second blog post..."
python3 publish_blog.py

echo "Full automation pipeline complete."
