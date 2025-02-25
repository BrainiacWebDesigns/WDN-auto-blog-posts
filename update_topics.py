import requests
from bs4 import BeautifulSoup
import os
import random

# Get the correct GitHub directory
script_dir = "C:\\Users\\doug\\WDN-auto-blog-posts"

# Define the full path to topics.txt
topics_file = os.path.join(script_dir, "topics.txt")

# Ensure topics.txt exists before trying to read from it
if not os.path.exists(topics_file):
    print("❌ ERROR: topics.txt not found. Creating a new one...")
    open(topics_file, "w").close()  # Create an empty file

# URLs to scrape trending topics from
sources = [
    "https://trends.google.com/trends/trendingsearches/daily",
    "https://www.searchenginejournal.com/category/seo/",
    "https://www.smashingmagazine.com/category/web-design/",
    "https://www.creativebloq.com/graphic-design",
]

def fetch_trending_topics():
    trending_topics = []

    for url in sources:
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, "lxml")

            # Extract headlines as trending topics
            for h2 in soup.find_all("h2"):
                topic = h2.text.strip()
                if topic and len(topic) > 5:
                    trending_topics.append(topic)

        except Exception as e:
            print(f"⚠️ Error scraping {url}: {e}")

    return list(set(trending_topics))  # Remove duplicates

# Load existing topics
with open(topics_file, "r", encoding="utf-8") as file:
    current_topics = set(file.read().splitlines())

# Fetch new trending topics
new_topics = fetch_trending_topics()

# Select 5 new trending topics
topics_to_add = [topic for topic in new_topics if topic not in current_topics]
topics_to_add = random.sample(topics_to_add, min(5, len(topics_to_add)))

# Append new topics to topics.txt
if topics_to_add:
    with open(topics_file, "a", encoding="utf-8") as file:
        for topic in topics_to_add:
            file.write(f"\n{topic}")

    print(f"✅ Added {len(topics_to_add)} new trending topics to topics.txt!")
else:
    print("❌ No new unique trending topics found.")