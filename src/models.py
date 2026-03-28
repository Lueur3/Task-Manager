class Task:
    def __init__(self, title: str, description: str, is_done: bool = False) -> None:
        self.title = title
        self.description = description
        self.is_done = is_done

    def mark_done(self):
        self.is_done = True

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "is_done": self.is_done,
        }

    @classmethod
    def from_dict(cls, task_dict: dict):

        task_title = task_dict.get("title", "")
        task_description = task_dict.get("description", "")
        task_is_done = task_dict.get("is_done", False)

        return cls(task_title, task_description, task_is_done)

    def __str__(self) -> str:
        return f"\nTask: {self.title}\nStatus: {self.is_done}"

    def __repr__(self) -> str:
        return f"\nTask: {self.title}\nDescription: {self.description}\nStatus: {self.is_done}"


class ToDoList:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, index: int):
        if index < 0 or index > len(self.tasks) - 1:
            raise ValueError("Wrong index!")

        del self.tasks[index]

    def get_all_tasks(self) -> list:
        return self.tasks

    def get_task(self, index: int):
        if index < 0 or index > len(self.tasks) - 1:
            raise ValueError("Wrong index!")
        return self.tasks[index]
