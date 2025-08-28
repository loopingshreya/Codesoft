def main():
    tasks = [] 
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))

            for _ in range(n_tasks):
                task_name = input("Enter the task: ")
                tasks.append({"task": task_name, "done": False})
                print("Task added!")

        elif choice == '2':
            if not tasks:
                print("\nNo tasks available!")
            else:
                print("\nTasks:")
                for index, t in enumerate(tasks):
                    status = "Done" if t["done"] else "Not Done"
                    print(f"{index + 1}. {t['task']} - {status}")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done!")
            else:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print(f"Task '{tasks[task_index]['task']}' marked as done!")
                else:
                    print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
