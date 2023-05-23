#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress

   REQUIREMENTS:
   You must use urllib or requests module
   The script must accept an integer as a parameter, which is the employee ID
   The script must display on the standard output the employee TODO list
   progress in this exact format:
   First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS
   /TOTAL_NUMBER_OF_TASKS):
   EMPLOYEE_NAME: name of the employee
   NUMBER_OF_DONE_TASKS: number of completed tasks
   TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
   and non-completed tasks
   Second and N next lines display the title of completed tasks: TASK_TITLE
   (with 1 tabulation and 1 space before the TASK_TITLE)
   """

import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]

    # response = requests.get(url)
    url_id = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_1 = requests.get(url_id)

    url_task = url_id + "/todos"
    response_2 = requests.get(url_task)

    if response_1.status_code == 200:
        user_id = response_1.json()
        user_name = user_id.get("name")
        user_task = response_2.json()
        task = []
        for i in user_task:
            if i.get("completed"):
                task.append(i)
        titles = []
        for j in user_task:
            if j.get("completed"):
                titles.append(j.get("title"))
        print("Employee {} is done with tasks\
        ({}/{}):".format(user_name, len(task), len(user_task)))
        for title in titles:
            print("\t{}".format(title))
