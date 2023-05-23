#!/usr/bin/python3
"""
   a Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress

   Extend the python script to export data in the json format

   REQUIREMENTS:
   Records all tasks that are owned by this employee
   Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
   TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task":
   "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
   "username": "USERNAME"}, ... ]}
   File name must be: USER_ID.json

   """

import json
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]

    url_id = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_1 = requests.get(url_id)

    url_task = url_id + "/todos"
    response_2 = requests.get(url_task)

    if response_1.status_code == 200:
        user_id = response_1.json()
        user_name = user_id.get("username")
        user_task = response_2.json()

        filename = f"{employee_id}.json"
        # Open the json file in write mode
        with open(filename, "w") as json_file:
            task = []
            for task in user_task:
                user_id = task["userId"]
                completed = task["completed"]
                title = task["title"]
                task_dic = {
                    "task": title,
                    "completed": completed
                    "username": user_name
                }
            # Write the data to json file
            json.dump({user:id: task_list}, json_file}
    else:
        print(f"Error: {response_1.status_code}")
