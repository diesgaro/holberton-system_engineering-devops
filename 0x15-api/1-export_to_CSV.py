#!/usr/bin/python3
'''
Python script that to export data in the CSV format.
Arguments:
    UserId = The Id of the user
Return:
    .csv file
'''


import csv
import requests
from sys import argv


if __name__ == "__main__":
    ''' Set user ID '''
    userId = argv[1]

    ''' Request users '''
    source_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        userId)
    data_user = requests.get(source_users).json()

    ''' Request ToDo '''
    source_todo = 'https://jsonplaceholder.typicode.com/todos'
    params_todo = {'userId': userId}
    data_todo = requests.get(source_todo, params=params_todo).json()

    ''' Make csv file '''
    with open('{}.csv'.format(data_user.get('id')), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for data in data_todo:
            temp_list = [
                data_user.get('id'),
                data_user.get('username'),
                data.get('completed'),
                data.get('title')
            ]
            writer.writerow(temp_list)
