#!/usr/bin/python3
"""
a module that queries the reddit Api
"""

import requests


def top_ten(subreddit):
    """
    Returns the titles a subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
            "User-Agent": "Subreddit Subscriber"
            }
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        for sub in data['data']['children']:
            print(sub['data']['title'])
    else:
        print(None)
