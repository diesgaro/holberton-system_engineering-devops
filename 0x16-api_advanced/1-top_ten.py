#!/usr/bin/python3
'''
Script that define a function to send request on Reddit Api
'''
import requests


def top_ten(subreddit):
    '''
    top_ten function that queryes and print the top 10 of titles
    for a given subreddit.
    Arguments:
        subreddit: subreddit to search
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    filters = {'limit': 10}

    req = requests.get(
        url,
        headers=headers,
        params=filters,
        allow_redirects=False
    )

    if (req.status_code is 200):
        list_top_10 = req.json().get('data').get('children')
        for title in list_top_10:
            print(title.get('data').get('title'))
    else:
        print(None)
