#!/usr/bin/python3
"""Gather data froman api"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    info = requests.get('https://jsonplaceholder.typicode.com/users')
    info = info.json()
    req = req.json()
    tasks = {tasks.get('title'): tasks.get('completed') for
             tasks in req if tasks.get('userId') == int(sys.argv[1])}
    for item in info:
        if item.get("id") == int(sys.argv[1]):
            name = item.get('name')
    num = sum(1 for v in tasks.values() if v is True)
    print('Employee {} is done with tasks ({}/{}):'.format
          (name, num, len(tasks)))
    for title, task in tasks.items():
        if task is True:
            print('{}'.format(title))
