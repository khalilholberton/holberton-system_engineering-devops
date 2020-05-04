#!/usr/bin/python3
"""Python script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress"""

if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user = requests.get(url + '/{}'.format(id)).json()
    todo = requests.get(url + '/{}/todos'.format(id)).json()
    tasks = []

    for task in todo:
        if task.get('completed') is True:
            tasks.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format
          (user.get('name'), len(tasks), len(todo)))
    for task in tasks:
        print('\t {}'.format(task))
