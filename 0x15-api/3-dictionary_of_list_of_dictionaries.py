#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
if __name__ == "__main__":
    import json
    import requests

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    user_dict = {}
    uname_dict = {}
    for user in users:
        u_id = user.get("id")
        user_dict[u_id] = []
        uname_dict[u_id] = user.get('username')
    for task in todo:
        task_dict = {}
        u_id = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict['username'] = uname_dict.get(u_id)
        user_dict.get(u_id).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsfile:
        json.dump(user_dict, jsfile)
