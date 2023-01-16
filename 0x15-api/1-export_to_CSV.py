#!/usr/bin/python3
"""Gather data froman api"""

import csv
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
    data_employee = []
    for title, task in tasks.items():
        infos = []
        infos.extend([sys.argv[1], name, task, title])
        data_employee.append(infos)

    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for inform in data_employee:
            writer.writerow(inform)
