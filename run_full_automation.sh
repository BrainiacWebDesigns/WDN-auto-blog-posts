#!/usr/bin/env bash
# Change to the directory where this script is located (repository root)
cd "$(dirname "$0")" || { echo "Failed to change directory to the script location."; exit 1; }

echo "Current directory: $(pwd)"

# Pull the latest changes from GitHub.
echo "Pulling latest changes..."
git pull origin main || { echo "Git pull failed."; exit 1; }

# Update trending topics.
echo "Updating trending topics..."
python3 update_topics.py || { echo "Failed to update trending topics."; exit 1; }

# Generate the first blog post.
echo "Generating first blog post..."
./generate_blog.sh || { echo "Failed to generate first blog post."; exit 1; }

# Generate the second blog post.
echo "Generating second blog post..."
./generate_blog.sh || { echo "Failed to generate second blog post."; exit 1; }

echo "Full automation script executed successfully."