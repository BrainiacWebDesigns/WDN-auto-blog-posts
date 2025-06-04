#!/usr/bin/env python3
try:
    import requests  # type: ignore
except Exception:  # pragma: no cover - fallback when requests isn't installed
    from urllib import request as _urllib_request

    class _Response:
        def __init__(self, text: str):
            self.text = text

    class _Requests:
        def get(self, url, headers=None):
            with _urllib_request.urlopen(url) as resp:
                return _Response(resp.read().decode("utf-8", errors="ignore"))

    requests = _Requests()

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover - use regex parser if bs4 isn't available
    import re

    def _extract_h2(html: str):
        pattern = re.compile(r"<h2[^>]*>(.*?)</h2>", re.IGNORECASE | re.DOTALL)
        for match in pattern.findall(html):
            text = re.sub(r"<[^>]+>", "", match).strip()
            if text:
                yield text

import os
import random

# Determine the directory where this script is located.
# This makes it work cross-platform without hard-coding a Windows path.
script_dir = os.path.abspath(os.path.dirname(__file__))

# Define the full path to topics.txt within the same directory.
topics_file = os.path.join(script_dir, "topics.txt")

# Ensure topics.txt exists before trying to read from it.
if not os.path.exists(topics_file):
    print("❌ ERROR: topics.txt not found. Creating a new one...")
    open(topics_file, "w").close()  # Create an empty file

# URLs to scrape trending topics from.
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
            if 'BeautifulSoup' in globals():
                soup = BeautifulSoup(response.text, "lxml")  # type: ignore[name-defined]
                # Extract headlines as trending topics from <h2> tags.
                for h2 in soup.find_all("h2"):
                    topic = h2.get_text(strip=True)
                    if topic and len(topic) > 5:
                        trending_topics.append(topic)
            else:
                for topic in _extract_h2(response.text):  # type: ignore[name-defined]
                    if len(topic) > 5:
                        trending_topics.append(topic)
        except Exception as e:
            print(f"⚠️ Error scraping {url}: {e}")
    return list(set(trending_topics))  # Remove duplicates

def update_topics():
    # Load existing topics.
    with open(topics_file, "r", encoding="utf-8") as file:
        current_topics = set(file.read().splitlines())

    # Fetch new trending topics.
    new_topics = fetch_trending_topics()

    # Select 5 new trending topics that are not already in current_topics.
    topics_to_add = [topic for topic in new_topics if topic not in current_topics]
    if topics_to_add:
        topics_to_add = random.sample(topics_to_add, min(5, len(topics_to_add)))
        with open(topics_file, "a", encoding="utf-8") as file:
            for topic in topics_to_add:
                file.write(f"\n{topic}")
        print(f"✅ Added {len(topics_to_add)} new trending topics to topics.txt!")
    else:
        print("❌ No new unique trending topics found.")

if __name__ == "__main__":
    update_topics()
