todo_list = []
def add_task(task):
    todo_list.append(task)
  print(f"Added:{task}"}

def show_tasks():
  print("\n--- My Tasks ---")
  for i, task in enumerate(todo_list,1):
    print(f"{i}. {task}"}

    add_task("Learn Python")
    add_task("Practice GitHub")
    add_task("Prepare for Outreachy")

show_tasks()
