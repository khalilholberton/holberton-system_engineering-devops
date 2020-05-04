#!/usr/bin/python3
"""
 Python script to export data in the JSON format.
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user = requests.get(url + '/{}'.format(id)).json()
    todo = requests.get(url + '/{}/todos'.format(id)).json()

    tasks = []
    for task in todo:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = user.get('username')
        tasks.append(task_dict)

    jsonfile = {}
    jsonfile[id] = tasks
    with open("{}.json".format(id), 'w') as f:
        json.dump(jsonfile, f)
