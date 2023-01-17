#!/usr/bin/python3
"""Gather data froman api"""

import json
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
            name = item.get('username')
    infos = []
    for title, task in tasks.items():
        dic_info = {"task": title, "completed": task, "username": name}
        infos.append(dic_info)
    data_employee = {}
    data_employee[sys.argv[1]] = infos

    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        json.dump(data_employee, f)
