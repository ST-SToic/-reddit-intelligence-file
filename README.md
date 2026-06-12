# Reddit Intelligence API Tool

## Overview
This project collects publicly available Reddit posts and comments using the official Reddit API. It is designed for research and analytics purposes, including sentiment analysis and trend discovery.

## Purpose
The goal of this tool is to help analyze public discussions on Reddit to identify:
- Topic trends
- Sentiment patterns
- Emerging discussions
- Research insights

This is strictly a read-only data collection tool.

## Features
- Fetch posts from selected subreddits
- Search posts by keywords
- Collect comments for analysis
- Basic sentiment / text processing support
- Export structured JSON data

## Tech Stack
- Python
- Reddit API (PRAW)

## Data Usage Policy
This project only accesses publicly available Reddit content via the official API.  
No private data is collected.  
No automated posting, voting, or messaging is performed.

## Setup

```bash
git clone https://github.com/yourusername/reddit-intelligence-api
cd reddit-intelligence-api
pip install -r requirements.txt
```

## Environment

Create `.env` file:
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=

## Run
python src/scraper.py

## Disclaimer
For research and educational purposes only.
