#!/usr/bin/env bash
# Change to the directory where this script is located (repository root)
cd "$(dirname "$0")" || { echo "Failed to change directory to the script location."; exit 1; }

echo "Current directory: $(pwd)"

# Pull the latest changes from GitHub.
echo "Pulling latest changes..."
git pull origin main || { echo "Git pull failed."; exit 1; }

# Check if topics.txt exists and is not empty; if so, select a random topic, otherwise use a default.
if [ -s topics.txt ]; then
    topic=$(shuf -n 1 topics.txt)
    echo "Selected topic: $topic"
else
    topic="The Future of SEO"
    echo "topics.txt is empty or missing. Using default topic: $topic"
fi

echo "Generating blog post for topic: $topic"
# Run the AI post generation script with the chosen topic.
python3 generate_ai_post.py "$topic" || { echo "Failed to generate blog post."; exit 1; }

# Verify that blog_post.txt was created.
if [ -f blog_post.txt ]; then
    echo "Blog post generated successfully."
else
    echo "Error: blog_post.txt not found."
    exit 1
fi

echo "Blog generation complete."
exit 0