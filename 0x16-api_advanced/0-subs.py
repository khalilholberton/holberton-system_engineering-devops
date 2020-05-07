#!/usr/binpython3
# This module contain the function number_of_subscribers

import requests as myreq


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    custom_user = {'User-agent': 'Khalil'}

    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    query = myreq.get(URL, headers=custom_user)

    if query.status_code != 200:
        return 0

    response = query.json()

    try:
        return response.get('data').get('subscribers')
    except Exception:
        return 0
