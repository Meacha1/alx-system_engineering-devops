#!/usr/bin/python3
'''Script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress
'''
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python todo.py EMPLOYEE_ID")
    sys.exit(1)

employee_id = sys.argv[1]
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    sys.exit(1)

todos = response.json()
completed_todos = [todo for todo in todos if todo["completed"]]
employee_name = todos[0]["user"]["name"]
num_completed_todos = len(completed_todos)
total_todos = len(todos)

print(f"Employee {employee_name} is done with {num_completed_todos}/{total_todos} tasks:")
for todo in completed_todos:
    print(f"\t {todo['title']}")
