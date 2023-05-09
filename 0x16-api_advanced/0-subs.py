#!/usr/bin/python3
'''
queries the Reddit API and returns the number of subscribers
for a given subreddit
'''
import requests


def number_of_subscribers(subreddit):
    '''returns the number of subscribers'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
