#!/usr/bin/python3
""" This module contain the function recurse """

import requests as myreq


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for
    the given subreddit, the function should return None
    """
    custom_user = {"User-agent": 'khalil'}

    myparams = {"after": after}

    query = myreq.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers=custom_user, params=myparams)

    if query.status_code is 404:
        return (None)

    for i in query.json()['data']['children']:
        hot_list.append(i['data']['title'])

    if query.json()['data']['after'] is not None:
        recurse(subreddit, hot_list, query.json()['data']['after'])
    return(hot_list)
