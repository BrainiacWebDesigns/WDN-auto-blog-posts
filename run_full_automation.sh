#!/bin/bash

# Load environment variables properly
set -a
source /home/doug/WDN-auto-blog-posts/.env
set +a

# Debugging - Print loaded credentials
echo "WP_USERNAME='$WP_USERNAME'"
echo "WP_PASSWORD Length: ${#WP_PASSWORD}"

# Activate virtual environment before running any Python script
source ~/WDN-auto-blog-posts/venv/bin/activate

# Navigate to the project directory
cd /home/doug/WDN-auto-blog-posts || exit

# Pull latest changes from GitHub
echo "Pulling latest changes..."
git pull origin main

# Update trending topics
echo "Updating trending topics..."
python3 update_topics.py

echo "Generating first blog post..."
# Read a topic from topics.txt
TOPIC=$(head -n 1 topics.txt)
if [ -z "$TOPIC" ]; then
    echo "❌ No topics found in topics.txt!"
    exit 1
fi

# Generate blog post using AI
echo "Generating blog post for topic: $TOPIC"
python3 generate_ai_post.py "$TOPIC"

# Check if blog_post.txt exists and has content
if [ ! -s blog_post.txt ]; then
    echo "❌ No content generated! Exiting."
    exit 1
fi

echo "Publishing blog post..."
python3 publish_blog.py

# Verify if publish_blog.py succeeded
if [ $? -ne 0 ]; then
    echo "❌ Blog post failed to publish!"
    exit 1
fi

echo "✅ Blog post successfully published!"

# Remove the used topic from topics.txt to avoid duplication
sed -i '1d' topics.txt

# Push changes back to GitHub
git add topics.txt
git commit -m "Updated topics.txt after posting"
git push origin main

echo "✅ Full automation script executed successfully."
