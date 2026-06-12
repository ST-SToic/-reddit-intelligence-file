from reddit_client import create_client

def scrape_subreddit(subreddit_name="python", limit=5):
    reddit = create_client()
    subreddit = reddit.subreddit(subreddit_name)

    data = []

    for post in subreddit.hot(limit=limit):
        data.append({
            "title": post.title,
            "score": post.score,
            "url": post.url
        })

    return data


if __name__ == "__main__":
    results = scrape_subreddit("python", 5)
    for r in results:
        print(r)
