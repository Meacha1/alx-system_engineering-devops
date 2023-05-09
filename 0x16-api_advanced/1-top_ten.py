#!/usr/bin/python3
''' Module 2 '''


import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the top 10 hot posts
    of the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python Reddit API Script"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        data = response.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
