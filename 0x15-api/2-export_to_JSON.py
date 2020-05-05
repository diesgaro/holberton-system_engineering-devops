#!/usr/bin/python3
'''
Python script that to export data in the JSON format.
Arguments:
    UserId = The Id of the user
Return:
    .json file
'''


import json
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

    ''' Make json file '''
    tasks = []
    for data in data_todo:
        temp_dict = {
            "task": data.get('title'),
            "completed": data.get('completed'),
            "username": data_user.get('username')
        }
        tasks.append(temp_dict)

    tasks_to_json = {data_user.get('id'): tasks}

    with open('{}.json'.format(data_user.get('id')), 'w') as file:
        file.write(json.dumps(tasks_to_json))
