#!usr/bin/python3
"""A moodule that queries tne REDDIT API"""

import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the REDDIT API

    arg:
        subreddit

    Returns:
        number of subscribers if True, else Zero
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Subreddit subscriber"
            }
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        subscribers = data["data"]["subscribers"]
    else:
        subscribers = 0
    return subscribers
