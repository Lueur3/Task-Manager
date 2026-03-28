import models as md
import storage as st
import sys

STORAGE_PATH = "data/tasks.json"

todo_list = st.load_from_json(STORAGE_PATH)


def show_menu():
    print("\nMenu:")
    print("1. Show all tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Get task")
    print("5. Complete the task")
    print("0. Exit")


print("Welcome to Task Manager!")

while True:
    try:
        show_menu()
        user_choice = int(input("\nYour choice: "))
        match user_choice:
            case 1:  # show all tasks
                user_tasks = todo_list.get_all_tasks()

                if user_tasks:
                    print("Index\tTask")
                    for index, task in enumerate(user_tasks):
                        print(f"{index}\t{task}")
                else:
                    print("You have no tasks.")
            case 2:  # add task

                while True:
                    user_task_title = input("Enter the task name: ")
                    if not user_task_title.strip():
                        print("the task title cannot be empty!")
                    else:
                        break

                user_task_description = input("Enter the task description:\n")
                user_task = md.Task(user_task_title, user_task_description)
                todo_list.add_task(user_task)
                st.save_to_json(todo_list, STORAGE_PATH)

            case 3:  # delete task
                task_index_del = int(input("Enter the index of the task to delete: "))
                todo_list.remove_task(task_index_del)
                st.save_to_json(todo_list, STORAGE_PATH)

            case 4:  # get task
                task_index = int(input("Enter the index of the task: "))
                user_task = todo_list.get_task(task_index)
                print(user_task.show_task())

            case 5:  # complete task
                task_index_compl = int(
                    input("Enter the index of the task to complete: ")
                )
                todo_list.get_task(task_index_compl).mark_done()
                st.save_to_json(todo_list, STORAGE_PATH)

            case 0:  # exit
                sys.exit()
    except (ValueError, IndexError):
        print("Input error or incorrect index!")

    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
