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
    dict_employee = {}
    for i in range(1, 11):
        for item in info:
            if item.get("id") == i:
                name = item.get('name')
        tasks = []
        for task in req:
            tasks.append({"username": name, "task": task.get('title') , "completed": task.get('completed')})
        dict_employee[i] = tasks


    with open('todo_all_employees.json', 'w') as f:
        json.dump(dict_employee, f)
