#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import json
    import csv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user = requests.get(url + '/{}'.format(id)).json()
    todo = requests.get(url + '/{}/todos'.format(id)).json()

    with open("{}.csv".format(id), 'w', newline='') as csv_file:
        filler = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            filler.writerow([id,
                              user.get('username'),
                              task.get('completed'),
                              task.get('title')])
