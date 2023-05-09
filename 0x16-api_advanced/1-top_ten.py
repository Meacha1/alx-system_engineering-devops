#!/usr/bin/python3
''' Module 2 '''
import requests


def top_ten(subreddit):
    '''queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
