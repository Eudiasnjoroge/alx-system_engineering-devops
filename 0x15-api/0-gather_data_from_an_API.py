#!/usr/bin/python3
"""
Fetch and display TODO list progress for a given employee ID using a REST API.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetch and display the TODO list progress of an employee."""
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information
    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        return
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Fetch user TODO list
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    
    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)
    
    # Print results
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
