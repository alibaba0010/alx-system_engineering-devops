#!/usr/bin/python3
"""
extend Python script to export data in CSV format
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todoss?userId={}".format(userId)).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            my_writer.writerow([int(userId), user.get('username'),
                                task.get('completed'),
                                task.get('title')])
