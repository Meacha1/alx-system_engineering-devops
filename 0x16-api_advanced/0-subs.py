#!/usr/bin/python3
'''
queries the Reddit API and returns the number of subscribers
for a given subreddit
'''


def number_of_subscribers(subreddit):
    '''returns the number of subscribers'''
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return data['data']['subscribers']
