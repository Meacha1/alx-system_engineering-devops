#!/usr/bin/python3
"""Module for task recursion"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    import requests

    my_request = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if my_request.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in my_request.json()
                        .get("data")
                        .get("children")]

    info = my_request.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
