#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress

   Extend the python script to export data in the CSV format

   REQUIREMENTS:
   Records all tasks that are owned by this employee
   Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
   File name must be: USER_ID.csv

   """

import csv
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
        user_name = user_id.get("name")
        user_task = response_2.json()

        filename = f"{employee_id}.csv"
        # Open the csv file in write mode
        with open(filename, "w", newline="") as csv_file:
            # Create a CSV writer object
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in user_task:
                user_id = task.get("userId")
                completed = task.get("completed")
                title = task.get("title")
                # Write the data to CSV file
                writer.writerow([user_id, user_name, completed, title])
    else:
        print(f"Error: {response_1.status_code}")
