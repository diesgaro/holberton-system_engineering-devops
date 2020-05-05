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
    ''' Request users '''
    source_users = 'https://jsonplaceholder.typicode.com/users'
    data_users = requests.get(source_users).json()

    ''' Request ToDo '''
    source_todo = 'https://jsonplaceholder.typicode.com/todos'

    ''' Make json file '''
    tasks_for_user = {}
    for users in data_users:
        params_todo = {'userId': users.get('id')}
        data_todo = requests.get(source_todo, params=params_todo).json()
        tasks = []
        for data in data_todo:
            temp_dict = {
                "task": data.get('title'),
                "completed": data.get('completed'),
                "username": users.get('username')
            }
            tasks.append(temp_dict)
        tasks_for_user.update({users.get('id'): tasks})

    with open('todo_all_employees.json', 'w') as file:
        file.write(json.dumps(tasks_for_user))
