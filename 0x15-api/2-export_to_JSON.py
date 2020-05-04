#!/usr/bin/python3
"""
 Python script to export data in the JSON format.
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?ID={}".
                        format(id), verify=False).json()
    username = user.get('username')
    tasks_list = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks_list.append(task_dict)

    js_task = {}
    js_task[id] = tasks_list
    with open("{}.json".format(id), 'w') as jsfile:
        json.dump(js_task, jsfile)
