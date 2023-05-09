#!/usr/bin/python3
''' Module 3'''


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""
    import requests
    headers = {"User-Agent": "Python Reddit API Script"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        posts = data["children"]
        after = data["after"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
