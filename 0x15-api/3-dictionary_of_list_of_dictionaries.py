#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

if __name__ == "__main__":
    import requests
    import json

    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    todo = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    finaljs = {}

    for user in users:
        id = user.get("id")
        username = user.get("username")
        list = []

        for task in todo:
            if (task.get("userId") == id and task.get("completed")):
                d = {}
                d["task"] = task.get("title")
                d["completed"] = task.get("completed")
                d["username"] = username
                list.append(d)

        finaljs[id] = list

    with open("todo_all_employees.json", 'w+') as jsfile:
        json.dump(finaljs, jsfile)
