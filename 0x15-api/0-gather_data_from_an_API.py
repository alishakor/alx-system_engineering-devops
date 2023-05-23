#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]

    #response = requests.get(url)
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
            if i.get("completed") == True:
                task.append(i)
        titles = []
        for j in user_task:
            if j.get("completed") == True:
                titles.append(j.get("title"))
        print("Employee {} is done with tasks({}/{}):".format(user_name, len(task), len(user_task)))
        for title in titles:
            print("\t{}".format(title))
