#!/usr/bin/python3
'''
Python script that using a REST API for a given user ID
Arguments:
    UserId = The Id of the user
Return:
    information about his/her ToDo list progress.
'''


import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    source_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        userId)

    source_todo = 'https://jsonplaceholder.typicode.com/todos'
    params_todo = {'userId': userId}

    data_user = requests.get(source_users).json()
    data_todo = requests.get(source_todo, params=params_todo).json()

    task_done = 0
    task_total = 0
    list_todo = []

    for data in data_todo:
        task_total += 1
        if data.get('completed'):
            task_done += 1
            list_todo.append('\t {}'.format(data.get('title')))

    print("Employee {} is done with tasks({}/{}):".format(
            data_user.get('name'),
            task_done,
            task_total
        )
    )

    print(*list_todo, sep='\n')
