#!/usr/bin/python3
"""Module 0"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    my_request = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                              .format(subreddit),
                              headers={"User-Agent": "My-User-Agent"},
                              allow_redirects=False)
    if my_request.status_code >= 300:
        print('None')
    data = my_request.json()["data"]["children"]
    for post in data:
        print(post["data"]["title"])
