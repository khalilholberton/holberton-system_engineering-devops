#!/usr/bin/python3
"""
 Python script to export data in the JSON format.
"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    id = sys.argv[1]
    user = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                        .format(id)).json().get("username")
    todo = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    mylist = []
    for task in todo:
        if (task.get("userId") == int(id)):
            d = {}
            d["task"] = task.get("title")
            d["completed"] = task.get("completed")
            d["username"] = user
            mylist.append(d)

    with open("{}.json".format(id), 'w+') as jsonfile:
        json.dump({id: mylist}, jsonfile)
