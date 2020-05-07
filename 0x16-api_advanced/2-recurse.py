#!/usr/bin/python3
'''
Script that define a function to send request on Reddit Api
'''
import requests


def recurse(subreddit, hot_list=[], last_item=None):
    '''
    top_ten function that queryes and print the top 10 of titles
    for a given subreddit.
    Arguments:
        subreddit: subreddit to search
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    filters = {'after': last_item, 'limit': 100}

    req = requests.get(
        url,
        headers=headers,
        params=filters,
        allow_redirects=False
    )

    if (req.status_code is 200):
        list_titles = req.json().get('data').get('children')
        for title in list_titles:
            hot_list.append(title.get('data').get('title'))

        last_item = req.json().get('data').get('after')

        if (last_item):
            recurse(subreddit, hot_list, last_item)
        return(hot_list)
    else:
        return(None)
