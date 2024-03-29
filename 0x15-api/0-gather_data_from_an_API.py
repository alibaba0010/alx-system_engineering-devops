#!/usr/bin/python3
"""getting data from an api
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos", params={"userId": userId}).json()
    completed_tasks = []
    for task in todos:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todos)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
