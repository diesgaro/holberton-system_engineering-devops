#!/usr/bin/python3
'''
Script that define a function to send request on Reddit Api
'''
import requests


def number_of_subscribers(subreddit):
    '''
    number_of_subscribers function that queryes the number of subscribers
    for a given subreddit.
    Arguments:
        subreddit: subreddit to search
    Return:
        A number with the total of subscribers, otherwise 0
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if (req.status_code is 200):
        return (req.json().get('data').get('subscribers'))
    else:
        return (0)
