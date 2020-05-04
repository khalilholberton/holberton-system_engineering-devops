#!/usr/bin/python3
"""
 Python script to export data in the JSON format.
"""

import requests
from sys import argv
import json

if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_dict = {}
    uname_dict = {}
    for user in users:
        user_id = user.get('id')
        user_dict[user_id] = []
        uname_dict[user_id] = user.get('username')

    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for task in todo:
        task_dict = {}
        user_id = task.get('userId')
        task_dict['username'] = uname_dict.get(user_id)
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        user_dict.get(user_id).append(task_dict)

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
