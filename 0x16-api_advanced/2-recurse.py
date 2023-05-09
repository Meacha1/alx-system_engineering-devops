#!/usr/bin/python3
''' Module 3'''


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"count": count, "after": after}
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()["data"]
    hot_list += [post["data"]["title"] for post in data["children"]]

    if data["after"] is None:
        return hot_list

    return recurse(subreddit, hot_list, count=count+1, after=data["after"])
