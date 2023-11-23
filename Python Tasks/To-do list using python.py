class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("-----------------")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Quit")

        choice = input("Enter the number of the operation you want to perform: ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid operation!")


if __name__ == "__main__":
    main()