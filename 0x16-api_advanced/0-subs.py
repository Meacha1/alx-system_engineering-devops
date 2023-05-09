#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    my_request = requests.get("https://www.reddit.com/r/{}/about.json"
                              .format(subreddit),
                              headers={"User-Agent": "My-User-Agent"},
                              allow_redirects=False)
    if my_request.status_code >= 300:
        return 0
    data = my_request.json()
    return data['data']['subscribers']
