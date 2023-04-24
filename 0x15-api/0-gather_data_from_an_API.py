#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_employee_todos(employee_id):
    # Define API endpoint and retrieve user info
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(base_url + f"users/{employee_id}")
    user_info = user_response.json()

    # Retrieve user's TODO list
    todos_response = requests.get(base_url + "todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Get list of completed task titles
    completed_tasks = [task['title'] for task in todos if task['completed']]

    # Print employee's progress report
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)
    print(f"Employee {user_info['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo.py EMPLOYEE_ID")
        sys.exit(1)
    employee_id = sys.argv[1]
    get_employee_todos(employee_id)
