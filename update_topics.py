import requests
from bs4 import BeautifulSoup
import random

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

            # Extract trending topics (modify based on site structure)
            for h2 in soup.find_all("h2"):
                topic = h2.text.strip()
                if topic and len(topic) > 5:
                    trending_topics.append(topic)

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    return list(set(trending_topics))  # Remove duplicates

# Load current topics
with open("topics.txt", "r") as file:
    current_topics = file.read().splitlines()

# Fetch new trending topics
new_topics = fetch_trending_topics()

# Select 5 new trending topics and add them to topics.txt
if new_topics:
    selected_topics = random.sample(new_topics, min(5, len(new_topics)))
    with open("topics.txt", "a") as file:
        for topic in selected_topics:
            file.write(f"\n{topic}")

    print(f"✅ Added {len(selected_topics)} new trending topics!")
else:
    print("❌ No new trending topics found.")