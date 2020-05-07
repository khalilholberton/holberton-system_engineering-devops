#!/usr/bin/python3
"""
This module contain the function top_ten
"""

import requests as myreq


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    custom_user = {'User-agent': 'Khalil'}

    URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    query = myreq.get(URL, headers=custom_user, allow_redirects=False)

    if query.status_code != 200:
        print(None)

    response = query.json()
    v = response.get('data').get('children')

    try:
        for d in v:
            print(d.get('data').get('title'))
    except Exception:
        print(None)
