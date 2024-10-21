import argparse
from database import TodoDatabase

def add_task(db, task, category):
    db.add_task(task, category)  # Pastikan ini memanggil add_task
    print(f"Task '{task}' has been added to the category '{category}'.")

def view_tasks(db, status=None, category=None):
    tasks = db.fetch_tasks(status, category)
    for task in tasks:
        print(task)

def complete_task(db, task_id):
    db.update_task_status(task_id, True)

def edit_task(db, task_id, new_task, new_category):
    db.update_task(task_id, new_task, new_category)
    print(f"Task {task_id} has been updated.")

def delete_task(db, task_id):
    db.delete_task(task_id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Todo List CLI")
    parser.add_argument('action', choices=['add', 'view', 'complete', 'delete', 'edit'], help="Action to perform")
    parser.add_argument('--id', type=int, help="ID of the task")
    parser.add_argument('--task', help="Task description")
    parser.add_argument('--category', help="Task category")
    args = parser.parse_args()

    db = TodoDatabase('todo.db')

    if args.action == 'add' and args.task:
        add_task(db, args.task, args.category)
    elif args.action == 'view':
        view_tasks(db)
    elif args.action == 'complete' and args.id:
        complete_task(db, args.id)
    elif args.action == 'delete' and args.id:
        delete_task(db, args.id)
    elif args.action == 'edit' and args.id and args.task:  # Pastikan ini ada
        edit_task(db, args.id, args.task, args.category)  # Panggil edit_task