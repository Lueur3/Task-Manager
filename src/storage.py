import models
import os
import json


def save_to_json(todo_list: models.ToDoList, file_path: str):
    folder_path = os.path.dirname(file_path)
    os.makedirs(folder_path, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        tasks_list = todo_list.get_all_tasks()
        data = [task.to_dict() for task in tasks_list]
        json.dump(data, f, indent=4)


def load_from_json(file_path: str) -> models.ToDoList:
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

            tasks_list = models.ToDoList()
            for task in data:
                tasks_list.add_task(models.Task.from_dict(task))

            return tasks_list

    return models.ToDoList()
