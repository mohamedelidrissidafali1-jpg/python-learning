# Simple To-Do List
print("=== To-Do List ===\n")

todos = []
completed_count = 0

while True:
    print("\n--- Menu ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    print("5. Complete task")
    print("6. Clear all tasks")
    
    choice = input("\nChoose option (1-6): ")

    if choice == "1":
        task = input("Enter task: ")
        todos.append(task)
        print(f"✓ Added: {task}")

    elif choice == "2":
        if len(todos) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(todos) == 0:
            print("No tasks to remove!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")

            index = int(input("Task number to remove: ")) - 1
            if 0 <= index < len(todos):
                removed = todos.pop(index)
                print(f"✓ Removed: {removed}")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    elif choice == "5":
        if len(todos) == 0:
            print("No tasks to complete!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")

            index = int(input("Task number to complete: ")) - 1

            if 0 <= index < len(todos):
                todos[index] = "[DONE] " + todos[index]
                completed_count += 1
                print(f"✓ Completed: {todos[index]}")
                print("Total completed:", completed_count)
            else:
                print("Invalid task number!")

    elif choice == "6":
        if len(todos) == 0:
            print("No tasks to clear!")
        else:
            todos.clear()
            print("All tasks cleared!")

    else:
        print("Invalid choice!")
